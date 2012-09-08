from collections import namedtuple

# General specification container for all tree nodes
NodeInfo = namedtuple('NodeInfo', ('format', 'arguments'))

StackData = namedtuple('StackData', ('data', 'precedence'))

# Substitute text returned by child's formatters, pick
# child using integer index specified in 'child'
FormatChild = namedtuple('FormatChild', ('child'))


# Same as FormatSubnode, but also specify custom precedence
FormatChildPrec = namedtuple('FormatChildPrec', ('child', 'precedence'))

FormatAttr = namedtuple('FormatAttr', ('attrname', 'child'))

FormatRangePrec = namedtuple('FormatRangePrec', ('first', 'last', 'separator', 'precedence'))


IndentCurrent = namedtuple('IndentCurrent', ())
