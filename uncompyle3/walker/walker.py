from uncompyle3.utils.spark import GenericASTTraversal
from uncompyle3.utils.debug import debug
from .arguments import NodeInfo, FormatChild, FormatChildPrec, FormatAttr, FormatRangePrec, IndentCurrent
from .exception import UnknownParameterError


TABLE_DIRECT = {
    # Binary operations
    'binary_expr':          NodeInfo('{} {} {}', (FormatChild(0), FormatChild(-1), FormatChild(1))),
    'BINARY_POWER':         NodeInfo('**', ()),
    'BINARY_MULTIPLY':      NodeInfo('*', ()),
    'BINARY_FLOOR_DIVIDE':  NodeInfo('//', ()),
    'BINARY_TRUE_DIVIDE':   NodeInfo('/', ()),
    'BINARY_MODULO':        NodeInfo('%', ()),
    'BINARY_ADD':           NodeInfo('+', ()),
    'BINARY_SUBTRACT':      NodeInfo('-', ()),
    'BINARY_LSHIFT':        NodeInfo('<<', ()),
    'BINARY_RSHIFT':        NodeInfo('>>', ()),
    'BINARY_AND':           NodeInfo('&', ()),
    'BINARY_XOR':           NodeInfo('^', ()),
    'BINARY_OR':            NodeInfo('|', ()),
    # Unary operations
    'unary_expr':           NodeInfo('{}{}', (FormatChild(1), FormatChild(0))),
    'UNARY_POSITIVE':       NodeInfo('+', ()),
    'UNARY_NEGATIVE':       NodeInfo('-', ()),
    'UNARY_INVERT':         NodeInfo('~', ()),
    'unary_not':            NodeInfo('not {}', (FormatChild(0),)),
    # Inplace operations
    'augassign':            NodeInfo('{}{} {} {}\n', (IndentCurrent(), FormatChild(0), FormatChild(2), FormatChild(1))),
    'INPLACE_POWER':        NodeInfo('**=', ()),
    'INPLACE_MULTIPLY':     NodeInfo('*=', ()),
    'INPLACE_FLOOR_DIVIDE': NodeInfo('//=', ()),
    'INPLACE_TRUE_DIVIDE':  NodeInfo('/=', ()),
    'INPLACE_MODULO':       NodeInfo('%=', ()),
    'INPLACE_ADD':          NodeInfo('+=', ()),
    'INPLACE_SUBTRACT':     NodeInfo('-=', ()),
    'INPLACE_LSHIFT':       NodeInfo('<<=', ()),
    'INPLACE_RSHIFT':       NodeInfo('>>=', ()),
    'INPLACE_AND':          NodeInfo('&=', ()),
    'INPLACE_OR':           NodeInfo('|=', ()),
    'INPLACE_XOR':          NodeInfo('^=', ()),
    # Miscellanea & temporary
    'call_function':        NodeInfo('{}({})', (FormatChild(0), FormatRangePrec(1, -1, ', ', 100))),
    'binary_subscr':        NodeInfo('{}[{}]', (FormatChild(0), FormatChildPrec(1, 100))),
    'call_stmt':            NodeInfo('{}{}\n', (IndentCurrent(), FormatChildPrec(0, 200))),
    'LOAD_NAME':            NodeInfo('{}', (FormatAttr('pattr', None),)),
    'LOAD_CONST':           NodeInfo('{}', (FormatAttr('pattr', None),)),
    'assign':               NodeInfo('{}{} = {}\n', (IndentCurrent(), FormatChild(-1), FormatChildPrec(0, 200))),
    'STORE_NAME':           NodeInfo('{}', (FormatAttr('pattr', None),)),
    'kwarg':                NodeInfo('{}={}', (FormatAttr('pattr', 0), FormatChild(1))),
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


class Walker(GenericASTTraversal):

    def __init__(self):
        self.indent = ''
        #self.prec = 100
        self.datastack = []
        GenericASTTraversal.__init__(self, ast=None)

    def gen_source(self, ast):
        self.traverse(ast)
        return ''.join(self.datastack)

    def traverse(self, node, indent=None):
        if indent is None:
            indent = ''
        self.preorder(node)

    def default(self, node):
        debug('walker.default({})'.format(''))
        table = TABLE_DIRECT
        key = node.type
        if key in table:
            self.engine(table[key], node)
            self.prune()
        else:
            debug('leaving walker.default(), no key')

    def engine(self, info, node):
        debug('walker.engine()')
        debug('entry: \"{}\"'.format(info))
        for arg in info.arguments:
            if isinstance(arg, IndentCurrent):
                debug("picked IndentCurrent")
                self.datastack.append(self.indent)
            elif isinstance(arg, FormatChild):
                debug("picked FormatChild")
                self.preorder(node[arg.child])
            elif isinstance(arg, FormatChildPrec):
                debug("picked FormatChildPrec")
                #p = self.prec
                #self.prec = arg.precedence
                self.preorder(node[arg.child])
                #self.prec = p
            elif isinstance(arg, FormatAttr):
                debug("picked FormatAttr")
                newnode = node[arg.child] if arg.child is not None else node
                self.datastack.append(getattr(newnode, arg.attrname))
            elif isinstance(arg, FormatRangePrec):
                debug("picked FormatRangePrec")
                #p = self.prec
                subnodes = node[arg.first:arg.last]
                subnodenum = len(subnodes)
                for subnode in subnodes:
                    self.preorder(subnode)
                if subnodenum == 0:
                    self.datastack.append('')
                else:
                    data = arg.separator.join(self.datastack[-subnodenum:])
                    del self.datastack[-subnodenum:]
                    self.datastack.append(data)
                #self.prec = p
            else:
                raise UnknownParameterError(arg)
        arglen = len(info.arguments)
        if arglen == 0:
            self.datastack.append(info.format)
        else:
            data = info.format.format(*self.datastack[-arglen:])
            del self.datastack[-arglen:]
            self.datastack.append(data)
            debug(self.datastack)
