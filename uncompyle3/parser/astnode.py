from collections import UserList


class ASTNode(UserList):
    def __init__(self, type_, children=[]):
        # TODO: consider intern()ing type string
        self.type = type_
        UserList.__init__(self, children)

#    def __getslice__(self, low, high):
#        return self.data[low:high]

    def __eq__(self, other):
        if isinstance(other, ASTNode):
            result = self.type == other.type and UserList.__eq__(self, other)
        else:
            result = self.type == other
        return result

    def __hash__(self):
        return hash(self.type)

    def __str__(self, indent=''):
        return self.__repr__(indent)

    def __repr__(self, indent=''):
        current = '{}{}'.format(indent, self.type)
        newindent = '  {}'.format(indent)
        children = '\n'.join(child.__str__(indent=newindent) for child in self)
        total = '{}\n{}'.format(current, children)
        return total
