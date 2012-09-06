class Token:

    def __init__(self, type_=None, attr=None, pattr=None, offset=None, linestart=None):
        # TODO: consider using intern()
        self.type = type_
        self.attr = attr
        self.pattr = pattr
        self.offset = offset
        self.linestart = linestart

    # TODO: rework reps and str methods
    def __repr__(self):
        return str(self.type)

    def __str__(self):
        pattr = self.pattr
        if self.linestart:
            return '\n%s\t%-17s %r' % (self.offset, self.type, pattr)
        else:
            return '%s\t%-17s %r' % (self.offset, self.type, pattr)

    def __hash__(self):
        return hash(self.type)

    def __getitem__(self, i):
        raise IndexError

    def __eq__(self, o):
        if isinstance(o, Token):
            # both are tokens: compare type and pattr
            return self.type == o.type or self.pattr == o.pattr
        else:
            return self.type == o
