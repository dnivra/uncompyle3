import re

from uncompyle3.utils.spark import GenericASTTraversal
from uncompyle3.utils.debug import debug
from .containers import NodeInfo, FormatChild, FormatRange, FormatAttr, IndentCurrent, IndentIncrease, IndentDecrease, Reformat, StackData
from .exception import UnknownParameterError


INDENT_STEP = ' ' * 4


TABLE_DIRECT = {
    # Binary operations
    #'binary_expr':          NodeInfo('{} {} {}', (FormatChild(0), FormatChild(-1), FormatChild(1))),
    'BINARY_POWER':         NodeInfo('**',),
    'BINARY_MULTIPLY':      NodeInfo('*',),
    'BINARY_FLOOR_DIVIDE':  NodeInfo('//',),
    'BINARY_TRUE_DIVIDE':   NodeInfo('/',),
    'BINARY_MODULO':        NodeInfo('%',),
    'BINARY_ADD':           NodeInfo('+',),
    'BINARY_SUBTRACT':      NodeInfo('-',),
    'BINARY_LSHIFT':        NodeInfo('<<',),
    'BINARY_RSHIFT':        NodeInfo('>>',),
    'BINARY_AND':           NodeInfo('&',),
    'BINARY_XOR':           NodeInfo('^',),
    'BINARY_OR':            NodeInfo('|',),
    # Unary operations
    'unary_expr':           NodeInfo('{}{}', (FormatChild(1), FormatChild(0))),
    'UNARY_POSITIVE':       NodeInfo('+',),
    'UNARY_NEGATIVE':       NodeInfo('-',),
    'UNARY_INVERT':         NodeInfo('~',),
    'unary_not':            NodeInfo('not {}', (FormatChild(0),)),
    # Inplace operations
    'augassign':            NodeInfo('{}{} {} {}\n', (IndentCurrent(), FormatChild(0), FormatChild(2), FormatChild(1))),
    'INPLACE_POWER':        NodeInfo('**=',),
    'INPLACE_MULTIPLY':     NodeInfo('*=',),
    'INPLACE_FLOOR_DIVIDE': NodeInfo('//=',),
    'INPLACE_TRUE_DIVIDE':  NodeInfo('/=',),
    'INPLACE_MODULO':       NodeInfo('%=',),
    'INPLACE_ADD':          NodeInfo('+=',),
    'INPLACE_SUBTRACT':     NodeInfo('-=',),
    'INPLACE_LSHIFT':       NodeInfo('<<=',),
    'INPLACE_RSHIFT':       NodeInfo('>>=',),
    'INPLACE_AND':          NodeInfo('&=',),
    'INPLACE_OR':           NodeInfo('|=',),
    'INPLACE_XOR':          NodeInfo('^=',),
    # Logic operations
    'and':                  NodeInfo('and',),
    'or':                   NodeInfo('or',),
    # Conditional branching & looping
    'ifstmt':               NodeInfo('{}if {}:\n{}{}{}', (IndentCurrent(), FormatChild(0), IndentIncrease(), FormatChild(1), IndentDecrease())),
    'ifelsestmt':           NodeInfo('{}if {}:\n{}{}{}{}else:\n{}{}{}', (IndentCurrent(), FormatChild(0), IndentIncrease(), FormatChild(1), IndentDecrease(), IndentCurrent(), IndentIncrease(), FormatChild(3), IndentDecrease())),
    'whilestmt':            NodeInfo('{}while {}:\n{}{}{}\n', (IndentCurrent(), FormatChild(1), IndentIncrease(), FormatChild(2), IndentDecrease())),
    'forstmt':              NodeInfo('{}for {} in {}:\n{}{}{}\n', (IndentCurrent(), FormatChild(4), FormatChild(1), IndentIncrease(), FormatChild(5), IndentDecrease())),
    # Miscellanea & temporary
    'call_function':        NodeInfo('{}({})', (FormatChild(0), FormatRange(1, -1, ', ', 100))),
    'binary_subscr':        NodeInfo('{}[{}]', (FormatChild(0), FormatChild(1, 100))),
    'call_stmt':            NodeInfo('{}{}\n', (IndentCurrent(), FormatChild(0, 200))),
    'LOAD_NAME':            NodeInfo('{}', (FormatAttr('pattr'),)),
    'LOAD_CONST':           NodeInfo('{}', (FormatAttr('pattr'),)),
    'assign':               NodeInfo('{}{} = {}\n', (IndentCurrent(), FormatChild(-1), FormatChild(0, 200))),
    'STORE_NAME':           NodeInfo('{}', (FormatAttr('pattr'),)),
    'kwarg':                NodeInfo('{}={}', (FormatAttr('pattr', 0, Reformat('^\'(?P<data>.*)\'$', '\g<data>')), FormatChild(1))),
    'compare':              NodeInfo('{} {} {}', (FormatChild(0, 19), FormatAttr('pattr', -1), FormatChild(1, 19))),
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

    'cmp':                  20,

    'unary_not':            22,

    'and':                  24,

    'or':                   26,
}


class Walker(GenericASTTraversal):

    def __init__(self):
        self.indent = ''
        self.datastack = []
        GenericASTTraversal.__init__(self, ast=None)

    def gen_source(self, ast):
        self.preorder(ast)
        return ''.join(item.data for item in self.datastack)

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
                word = StackData(self.indent)
                self.datastack.append(word)
            elif isinstance(arg, IndentIncrease):
                debug("picked IndentIncrease")
                self.indent += INDENT_STEP
                word = StackData('')
                self.datastack.append(word)
            elif isinstance(arg, IndentDecrease):
                self.indent = self.indent[:-4]
                word = StackData('')
                self.datastack.append(word)
            elif isinstance(arg, FormatChild):
                debug("picked FormatChild")
                self.preorder(node[arg.child])
                if arg.reformat is not None:
                    word_old = self.datastack[-1]
                    word_new = StackData(self.__reformat(arg.reformat, word_old.data), word_old.precedence)
                    self.datastack[-1] = word_new
            elif isinstance(arg, FormatRange):
                debug("picked FormatRangePrec")
                subnodes = node[arg.first:arg.last]
                subnodenum = len(subnodes)
                for subnode in subnodes:
                    self.preorder(subnode)
                if subnodenum == 0:
                    word = StackData('')
                else:
                    data = arg.separator.join(word.data for word in self.datastack[-subnodenum:])
                    del self.datastack[-subnodenum:]
                    if arg.reformat is not None:
                        data = self.__reformat(arg.reformat, data)
                    word = StackData(data)
                self.datastack.append(word)
            elif isinstance(arg, FormatAttr):
                debug("picked FormatAttr")
                newnode = node[arg.child] if arg.child is not None else node
                data = getattr(newnode, arg.attrname)
                if arg.reformat is not None:
                    data = self.__reformat(arg.reformat, data)
                word = StackData(data)
                self.datastack.append(word)
            else:
                raise UnknownParameterError(arg)
        arglen = len(info.arguments)
        if arglen == 0:
            word = StackData(info.format)
        else:
            data = info.format.format(*(word.data for word in self.datastack[-arglen:]))
            del self.datastack[-arglen:]
            word = StackData(data)
        self.datastack.append(word)
        debug("Engine:", self.datastack)

    def __reformat(self, reformat, data):
        return re.sub(reformat.match, reformat.sub, data)

    def n_binary_expr(self, node):
        # Run engine on child nodes to fill the stack
        # with ready-to-use data
        self.preorder(node[0])
        self.preorder(node[-1])
        self.preorder(node[1])
        # Get precedences and data for all involved parts
        p_left = self.datastack[-3].precedence
        p_right = self.datastack[-1].precedence
        p_oper = PRECEDENCE.get(node[-1][0].type)
        data_left = self.datastack[-3].data
        data_right = self.datastack[-1].data
        data_oper = self.datastack[-2].data
        # Start working on data. We enclose left part in parenthesis only when
        # its operation has bigger precedence, in case with equal precedence it's
        # implied that left part is executed first.
        if p_oper is not None and p_left is not None and p_left > p_oper:
            data_left = '({})'.format(data_left)
        # With right part we add parenthesis even in case of equal precedences -
        # despite it has the same arithemtical meaning with or without them,
        # python calculates parenthized part first, and we must reflect it
        # in the source
        if p_oper is not None and p_right is not None and p_right >= p_oper:
            data_right = '({})'.format(data_right)
        # Form word and modify the stack
        data = '{} {} {}'.format(data_left, data_oper, data_right)
        word_new = StackData(data, p_oper)
        del self.datastack[-3:]
        self.datastack.append(word_new)
        self.prune()

    def format_logic(self, node):
        # Almost the same as binary expression processing, with except for 2 things:
        # 1) Different layout of data within node
        # 2) Does not parenthize expressions on the right-hand, if they have
        # the same precedence as logical operator
        self.preorder(node[0])
        self.preorder(node[2])
        p_left = self.datastack[-2].precedence
        p_oper = PRECEDENCE.get(node.type)
        p_right = self.datastack[-1].precedence
        data_left = self.datastack[-2].data
        data_oper = TABLE_DIRECT.get(node.type).format
        data_right = self.datastack[-1].data
        if p_oper is not None and p_left is not None and p_left > p_oper:
            data_left = '({})'.format(data_left)
        if p_oper is not None and p_right is not None and p_right > p_oper:
            data_right = '({})'.format(data_right)
        data = '{} {} {}'.format(data_left, data_oper, data_right)
        word_new = StackData(data, p_oper)
        del self.datastack[-2:]
        self.datastack.append(word_new)
        self.prune()

    n_or = n_and = format_logic
