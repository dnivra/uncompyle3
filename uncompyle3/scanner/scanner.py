import marshal

from . import dis
from .token import Token


class Scanner:

    def run(self, bytecode):
        code_object = marshal.loads(bytecode)
        tokens = self.tokenize(code_object)
        return tokens

    def tokenize(self, co):
        """
        Convert code object into a sequence of tokens.

        Based on dis.disassemble() function.
        """
        tokens = []
        self.code = code = co.co_code
        linestarts = dict(dis.findlinestarts(co))
        n = len(code)
        extended_arg = 0
        free = None
        for offset in self.op_range(0, n):
            op = code[offset]
            current_token = Token()
            current_token.type = dis.opname[op]
            current_token.offset = offset
            current_token.linestart = True if offset in linestarts else False
            if op >= dis.HAVE_ARGUMENT:
                oparg = code[offset+1] + code[offset+2]*256 + extended_arg
                extended_arg = 0
                if op == dis.EXTENDED_ARG:
                    extended_arg = oparg*65536

                current_token.attr = oparg
                if op in dis.hasconst:
                    current_token.pattr = repr(co.co_consts[oparg])
                elif op in dis.hasname:
                    current_token.pattr = co.co_names[oparg]
                elif op in dis.hasjrel:
                    current_token.pattr = repr(offset + 3 + oparg)
                elif op in dis.haslocal:
                    current_token.pattr = co.co_varnames[oparg]
                elif op in dis.hascompare:
                    current_token.pattr = dis.cmp_op[oparg]
                elif op in dis.hasfree:
                    if free is None:
                        free = co.co_cellvars + co.co_freevars
                    current_token.pattr = free[oparg]
            tokens.append(current_token)
        return tokens

    def op_size(self, op):
        """
        Return size of operator with its arguments
        for given opcode.
        """
        if op < dis.HAVE_ARGUMENT:
            return 1
        else:
            return 3

    def op_range(self, start, end):
        """
        Iterate through positions of opcodes, skipping
        arguments.
        """
        while start < end:
            yield start
            start += self.op_size(self.code[start])
