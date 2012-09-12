from uncompyle3.scanner.token import Token
from uncompyle3.utils.spark import GenericASTTraversal


class TokenLocator(GenericASTTraversal):
    """
    Given AST, finds first token it encounters.
    """

    def __init__(self):
        self.result = None
        GenericASTTraversal.__init__(self, ast=None)

    def find_first(self, ast):
        self.result = None
        self.preorder(ast)
        return self.result

    def default(self, node):
        """
        Called on access to all nodes of AST.
        """
        # If we already have result, make sure
        # to not traverse further
        if self.result is not None:
            self.prune()
        if isinstance(node, Token):
            self.result = node
            self.prune()
