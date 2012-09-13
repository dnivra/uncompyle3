from .scanner.scanner import Scanner
from .scanner.token import Token
from .parser.parser import Parser
from .walker.walker import Walker
from .utils.debug import debug


class Uncompyle:

    def __init__(self):
        pass

    def run(self, file_bytes):
        ### File format check stage ###
        #magic = file_bytes[:4]
        #timestamp = file_bytes[4:8]
        bytecode = file_bytes[8:]

        ### Scanner stage ###
        scanner = Scanner()
        tokens = scanner.tokenize(bytecode)
        debug('---Tokens debug output---\n#: offset linestart type attr pattr')
        k = 1
        for i in tokens:
            debug('op {}:'.format(k), i.offset, i.linestart, i.type, i.attr, i.pattr)
            k+=1

        ### Parser stage ###
        # This is some kind of hack(?) taken from uncompyle 2 walker code
        debug('\n\n---Parser stage debug---')
        if len(tokens) > 2 and tokens[-1] == Token(type_='RETURN_VALUE') and tokens[-2] == Token(type_='LOAD_CONST'):
            del tokens[-2:]

        parser = Parser()
        ast = parser.parse(tokens)
        debug(ast)

        ### Walker stage ###
        debug('\n\n---Walker stage debug---')
        walker = Walker()
        return walker.gen_source(ast)
