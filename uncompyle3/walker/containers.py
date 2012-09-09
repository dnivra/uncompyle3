from collections import namedtuple


# General specification container for all tree nodes
NodeInfo = namedtuple('NodeInfo', ('format', 'arguments'))


# Get current indentation level
IndentCurrent = namedtuple('IndentCurrent', ())


# Get return value of child's formatters, optionally
# specify custom precedence
FormatChild = namedtuple('FormatChild', ('child', 'precedence', 'reformat'))


# Like FormatChild, but for range of children, adding separator
# between each
FormatRange = namedtuple('FormatRange', ('first', 'last', 'separator', 'precedence', 'reformat'))


# Get attribute value of current node, or of child when specified
FormatAttr = namedtuple('FormatAttr', ('attrname', 'child', 'reformat'))


# Reformat
Reformat = namedtuple('Reformat', ('match', 'sub'))
