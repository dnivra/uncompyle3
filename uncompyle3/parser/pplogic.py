from collections import OrderedDict

from uncompyle3.utils.spark import GenericASTTraversal
from .astnode import ASTNode
from .tokenlocator import TokenLocator


class PostProcessLogic(GenericASTTraversal):
    """
    As parser incorrectly generates tree structure for
    logic structures, this class is intended to fix it.
    """

    def __init__(self):
        GenericASTTraversal.__init__(self, ast=None)

    def repair(self, ast):
        self.preorder(ast)

    def n_expr(self, node):
        if self.contains_logic(node) is True:
            self.smash_node(node)
            self.layout(node)
            self.prune()

    def contains_logic(self, node):
        if node.type == 'expr' and len(node) == 1 and node[0].type == 'logic_expr':
            return True
        else:
            return False

    def smash_node(self, expr_node):
        """
        Transform tree with logic nodes into
        flat structure.
        """
        # Will serve as container for flattened data
        logic_expr = expr_node[0]
        # Logic node should always be composed of 3 children
        lh_expr, logic_op, rh_expr = logic_expr
        # Clean logic node
        del logic_expr[:]
        # If we're dealing with another logic expression,
        # we flatten it too and add to top-level logic
        # expression node
        self.smash_child_expr(logic_expr, lh_expr)
        logic_expr.append(logic_op)
        self.smash_child_expr(logic_expr, rh_expr)

    def smash_child_expr(self, parent, child_expr):
        """
        If passed child is logic expression too,
        smash it, then regardless of check append
        result to parent.
        """
        if self.contains_logic(child_expr) is True:
            self.smash_node(child_expr)
            parent += child_expr[0]
        else:
            # We need to traverse non-logic expression
            # branches to make sure nested logical trees
            # are fixed too
            self.preorder(child_expr)
            parent.append(child_expr)

    def get_token_map(self, node):
        """
        Go through children of passed node and
        compose map with first tokens of each child.
        """
        # Format: {token offset: token}
        token_map = OrderedDict()
        locator = TokenLocator()
        for child in node:
            token = locator.find_first(child)
            token_map[token.offset] = token
        return token_map

    def layout(self, expr_node):
        """
        Perform single step of structurizing of our
        flat list. Pick operand and 'raise' it.
        """
        logic_expr = expr_node[0]
        flat_len = len(logic_expr)
        # If we have simple single expr subnode,
        # just move contents of child to passed node
        if flat_len == 1:
            expr_node[:] = logic_expr[:]
        # When we have 5 or more elements in the flat structure,
        # we have to perform analysis on how to structurize tree
        elif flat_len >= 5:
            token_map = self.get_token_map(logic_expr)
            jumptargets = tuple(token_map.keys())
            # Assume we pick 1st logic operand for
            # division of list into tree with 2 branches
            pick_idx = 1
            for child_idx in range(flat_len):
                child = logic_expr[child_idx]
                # Skip all non-logic nodes
                if child.type != 'logic_op':
                    continue
                # Get jump destination of logic token and check
                # if it's within range of available jump targets.
                # If it's not there, it means that this node can
                # jump either to next expression, or to result,
                # which lies out of the scope of list being
                # processed, which means normal execultion flow,
                # and lack of need to pick new logic operator
                jump_dest = child[0].attr
                if jump_dest not in jumptargets:
                    continue
                # If we jump within given range, it means that normal
                # flow is broken and we should pick another logic node,
                # around which we'll structurize list. We should do it
                # on first encountered jump, as it's longest one (there
                # may be smaller, 'inner' jumps). This jump is performed
                # onto the first element of the top-level expression,
                # which in scope of logical expression means first element
                # of right-hand expression, with separator being one position
                # to the left, and remaining part being left-hand expression
                pick_idx = jumptargets.index(jump_dest) - 1
                break
            # Move logic op node to its proper position,
            # split flat list into two parts, place both
            # into new expr nodes, and add these expr nodes
            # to logic node. Also run method on split flat
            # parts to ensure they're processed too.
            flat_lh = logic_expr[:pick_idx]
            logic_op = logic_expr[pick_idx]
            flat_rh = logic_expr[pick_idx+1:]
            del logic_expr[:]
            expr_lh = ASTNode('expr')
            logic_expr_lh = ASTNode('logic_expr')
            expr_lh.append(logic_expr_lh)
            logic_expr_lh += flat_lh
            self.layout(expr_lh)
            logic_expr.append(expr_lh)
            logic_expr.append(logic_op)
            expr_rh = ASTNode('expr')
            logic_expr_rh = ASTNode('logic_expr')
            expr_rh.append(logic_expr_rh)
            logic_expr_rh += flat_rh
            self.layout(expr_rh)
            logic_expr.append(expr_rh)

