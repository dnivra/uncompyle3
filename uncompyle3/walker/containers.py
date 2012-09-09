from collections import namedtuple

# Here we use named tuples with overridden __new__ method to allow
# use of default values for certain arguments

# General specification container for all tree nodes
class NodeInfo(namedtuple('NodeInfo', ('format', 'arguments'))):
    def __new__(cls, format_, arguments=()):
        return tuple.__new__(cls, (format_, arguments))


# Get current indentation level
IndentCurrent = namedtuple('IndentCurrent', ())


# Get return value of child's formatters, optionally
# specify custom precedence
class FormatChild(namedtuple('FormatChild', ('child', 'precedence', 'reformat'))):
    def __new__(cls, child, precedence=None, reformat=None):
        return tuple.__new__(cls, (child, precedence, reformat))


# Like FormatChild, but for range of children, adding separator
# between each
class FormatRange(namedtuple('FormatRange', ('first', 'last', 'separator', 'precedence', 'reformat'))):
    def __new__(cls, first, last, separator, precedence=None, reformat=None):
        return tuple.__new__(cls, (first, last, separator, precedence, reformat))


# Get attribute value of current node, or of child when specified
class FormatAttr(namedtuple('FormatAttr', ('attrname', 'child', 'reformat'))):
    def __new__(cls, attrname, child=None, reformat=None):
        return tuple.__new__(cls, (attrname, child, reformat))


# Reformat string, pass both fields as 1st and 2nd args to re.sub()
Reformat = namedtuple('Reformat', ('match', 'sub'))
