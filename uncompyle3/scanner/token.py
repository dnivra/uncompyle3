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
        linestart = ' (linestart)' if self.linestart else ''
        return '{:<3} {:>15} {} {}{}'.format(self.offset, self.type, self.attr, self.pattr, linestart)

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
