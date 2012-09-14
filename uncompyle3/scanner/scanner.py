import marshal

from .dis import *
from .token import Token


class Scanner:

    def run(self, bytecode):
        code_object = marshal.loads(bytecode)
        tokens = self.tokenize(code_object, Token)
        return tokens

    def tokenize(self, co, token_cls):
        """Convert code object into a sequence of tokens."""
        tokens = []
        code = co.co_code
        linestarts = dict(findlinestarts(co))
        n = len(code)
        i = 0
        extended_arg = 0
        free = None
        while i < n:
            op = code[i]
            current_token = token_cls()
            current_token.type = opname[op]
            current_token.offset = i
            current_token.linestart = True if i in linestarts else False
            i = i+1
            if op >= HAVE_ARGUMENT:
                oparg = code[i] + code[i+1]*256 + extended_arg
                extended_arg = 0
                i = i+2
                if op == EXTENDED_ARG:
                    extended_arg = oparg*65536

                current_token.attr = oparg
                if op in hasconst:
                    current_token.pattr = repr(co.co_consts[oparg])
                elif op in hasname:
                    current_token.pattr = co.co_names[oparg]
                elif op in hasjrel:
                    current_token.pattr = repr(i + oparg)
                elif op in haslocal:
                    current_token.pattr = co.co_varnames[oparg]
                elif op in hascompare:
                    current_token.pattr = cmp_op[oparg]
                elif op in hasfree:
                    if free is None:
                        free = co.co_cellvars + co.co_freevars
                    current_token.pattr = free[oparg]
            tokens.append(current_token)
        return tokens
