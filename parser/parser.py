from utils.spark import GenericASTBuilder

from .astnode import ASTNode


class Parser(GenericASTBuilder):

    def __init__(self):
        GenericASTBuilder.__init__(self, ASTNode, "stmts")

    def p_grammar(self, args):
        """
        stmts ::= sstmt
        sstmt ::= stmt
        stmt ::= call_stmt
        call_stmt ::= expr POP_TOP
        """

    def p_expr(self, args):
        """
        expr ::= call_function
        expr ::= LOAD_NAME
        """

#    def p_custom(self, args):
#        """
#        call_function ::= expr CALL_FUNCTION
#        """
