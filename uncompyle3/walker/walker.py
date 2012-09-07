import re

from uncompyle3.utils.spark import GenericASTTraversal
from uncompyle3.utils.debug import debug


TABLE_R = {
     'CALL_FUNCTION': ('%c(%P)', 0, (1, -1, ', ', 100))
}
TABLE_DIRECT = {
    # Binary operations
    'BINARY_POWER':     ('**',),
    'BINARY_MULTIPLY':  ('*',),
    'BINARY_FLOOR_DIVIDE':   ('//',),
    'BINARY_TRUE_DIVIDE':   ('/',),
    'BINARY_MODULO':   ('%',),
    'BINARY_ADD':   ('+',),
    'BINARY_SUBTRACT':   ('-',),
    'BINARY_LSHIFT':   ('<<',),
    'BINARY_RSHIFT':   ('>>',),
    'BINARY_AND':   ('&',),
    'BINARY_XOR':   ('^',),
    'BINARY_OR':   ('|',),
    # Unary operations
    'unary_expr':   ( '%c%c', 1, 0),
    'UNARY_POSITIVE':    ( '+',),
    'UNARY_NEGATIVE':    ( '-',),
    'UNARY_INVERT':    ( '~%c'),
    'unary_not':    ( 'not %c', 0 ),
    # Inplace operations
    'augassign':    ( '%|%c %c %c\n', 0, 2, 1),
    'INPLACE_POWER':    ( '**=',),
    'INPLACE_MULTIPLY':    ( '*=' ,),
    'INPLACE_FLOOR_DIVIDE':    ( '//=' ,),
    'INPLACE_TRUE_DIVIDE':    ( '/=' ,),
    'INPLACE_MODULO':    ( '%%=',),
    'INPLACE_ADD':    ( '+=' ,),
    'INPLACE_SUBTRACT':    ( '-=' ,),
    'INPLACE_LSHIFT':    ( '<<=',),
    'INPLACE_RSHIFT':    ( '>>=',),
    'INPLACE_AND':    ( '&=' ,),
    'INPLACE_OR':    ( '|=' ,),
    'INPLACE_XOR':    ( '^=' ,),
    # Miscellanea & temporary
    'binary_subscr':    ( '%c[%p]', 0, (1,100)),
    'call_stmt':    ('%|%p\n', (0, 200)),
    'LOAD_NAME':    ('%{pattr}',),
    'assign':       ('%|%c = %p\n', -1, (0, 200)),
    'STORE_NAME':   ('%{pattr}',),
}


MAP_DIRECT = (TABLE_DIRECT, )
MAP_R = (TABLE_R, -1)

MAP = {
    'stmt':        MAP_R,
    'call_function':        MAP_R,
    'designator':    MAP_R,
}

PRECEDENCE = {
    'call_function':        2,

    'BINARY_POWER':         4,

    'BINARY_MULTIPLY':      8,
    'BINARY_DIVIDE':        8,
    'BINARY_TRUE_DIVIDE':   8,
    'BINARY_FLOOR_DIVIDE':  8,
    'BINARY_MODULO':        8,

    'BINARY_ADD':           10,
    'BINARY_SUBTRACT':      10,

    'BINARY_LSHIFT':        12,
    'BINARY_RSHIFT':        12,

    'BINARY_AND':           14,

    'BINARY_XOR':           16,

    'BINARY_OR':            18,
}

escape = re.compile(r"""
            (?P<prefix> [^%]* )
            % ( \[ (?P<child> -? \d+ ) \] )?
                ((?P<type> [^{] ) |
                 ( [{] (?P<expr> [^}]* ) [}] ))
        """, re.VERBOSE)



class Walker(GenericASTTraversal):

    def __init__(self):
        self.indent = ''
        self.result = ''
        self.prec = 100
        GenericASTTraversal.__init__(self, ast=None)

    def gen_source(self, ast):
        self.traverse(ast)

    def traverse(self, node, indent=None):
        if indent is None:
            indent = ''
        self.preorder(node)

    def default(self, node):
        debug('walker.default({})'.format(''))
        mapping = MAP.get(node, MAP_DIRECT)
        table = mapping[0]
        key = node
        debug('current key:', '\"{}\"'.format(key.type).replace('\n', '\\n'))
        # TODO: check if this part is still necessary
        for i in mapping[1:]:
            key = key[i]
            debug('updated key:', '\"{}\"'.format(key.type).replace('\n', '\\n'))

        if key in table:
            self.engine(table[key], node)
            self.prune()
        else:
            debug('leaving walker.default(), no key')

    def engine(self, entry, startnode):
        #self.print_('-----')
        #self.print_(str(startnode.__dict__))
        debug('walker.engine()')
        debug('entry: \"{}\"'.format(entry))

        fmt = entry[0]
        ## no longer used, since BUILD_TUPLE_n is pretty printed:
        ##lastC = 0
        arg = 1
        i = 0

        m = escape.search(fmt)
        while m:
            i = m.end()
            debug('writing prefix: \"{}\"'.format(m.group('prefix')))
            self.write(m.group('prefix'))

            typ = m.group('type') or '{'
            node = startnode
            try:
                if m.group('child'):
                    debug('using child')
                    node = node[int(m.group('child'))]
            except:
                print(node.__dict__)
                raise
            debug('type:', typ)
            if   typ == '%':    self.write('%')
            elif typ == '+':    self.indentMore()
            elif typ == '-':    self.indentLess()
            elif typ == '|':    self.write(self.indent)
            elif typ == 'p':
                p = self.prec
                (index, self.prec) = entry[arg]
                self.preorder(node[index])
                self.prec = p
                arg += 1
            elif typ == 'c':
                self.preorder(node[entry[arg]])
                arg += 1
            elif typ == 'P':
                p = self.prec
                low, high, sep, self.prec = entry[arg]
                remaining = len(node[low:high])
                ## remaining = len(node[low:high])
                for subnode in node[low:high]:
                    self.preorder(subnode)
                    remaining -= 1
                    if remaining > 0:
                        self.write(sep)
                self.prec = p
                arg += 1
            elif typ == '{':
                d = node.__dict__
                expr = m.group('expr')
                try:
                    self.write(eval(expr, d, d))
                except:
                    print(node)
                    raise
            m = escape.search(fmt, i)
        self.write(fmt[i:])

    def write(self, *data):
        debug('writing: \"{}\"'.format(''.join(data)))
        self.result += ''.join(data)


    def n_expr(self, node):
        debug('walker.n_expr()')
        p = self.prec
        if node[0].type.startswith('binary_expr'):
            n = node[0][-1][0]
        else:
            n = node[0]
        self.prec = PRECEDENCE.get(n,-2)
        debug('picked node {} with precedence {}, old precedence {}'.format(n.type, self.prec, p))
        if n == 'LOAD_CONST' and repr(n.pattr)[0] == '-':
            self.prec = 6
        if p < self.prec:
            self.write('(')
            self.preorder(node[0])
            self.write(')')
        else:
            self.preorder(node[0])
        self.prec = p
        self.prune()

    def n_LOAD_CONST(self, node):
        ## If original string contains singlequotes, replace them with
        ## bouble-quotes
        #data = re.sub("^'(?P<data>.*)'$", "\"\g<data>\"", node.pattr)
        self.write(node.pattr)
        self.prune()

    def n_binary_expr(self, node):
        self.preorder(node[0])
        self.write(' ')
        self.preorder(node[-1])
        self.write(' ')
        self.prec -= 1
        self.preorder(node[1])
        self.prec += 1
        self.prune()
