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

    def __repr__(self, indent=''):
        rv = str(self.type)
        for k in self:
            rv = rv + '\n' + str.replace(str(k), '\n', '\n  ')
        return rv
