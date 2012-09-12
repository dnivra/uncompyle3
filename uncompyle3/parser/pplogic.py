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
        if self.detect_logic_expr(node) is True:
            self.repair_logic(node)
            self.prune()

    def repair_logic(self, expr_node):
        """
        General workflow for repairing logic trees.
        """
        self.smash_node(expr_node)
        self.layout(expr_node)

    def smash_node(self, expr_node):
        """
        Transform tree with logic nodes into
        flat structure.
        """
        # Container for flattened data
        logic_node = expr_node[0]
        # Logic node should always be composed of 3 children
        lh_expr, _, rh_expr = logic_node
        # Remove both expression children from logic node
        del logic_node[0]
        del logic_node[1]
        # Remove logic node from expression node
        del expr_node[0]
        # If we're dealing with another logic expression,
        # we flatten it too and add to top-level logic
        # expression node
        self.smash_child_expr(expr_node, lh_expr)
        expr_node.append(logic_node)
        self.smash_child_expr(expr_node, rh_expr)

    def detect_logic_expr(self, node):
        """
        Given expression node, attempts to find out
        if its top-level children are dealing with
        logic.
        """
        if node.type == 'expr' and len(node) == 1 and node[0].type in ('and', 'or'):
            return True
        else:
            return False

    def smash_child_expr(self, parent, child):
        """
        If passed child is logic expression too,
        smash it, then regardless of check append
        result to parent.
        """
        if self.detect_logic_expr(child) is True:
            self.smash_node(child)
            parent += child
        else:
            # We need to traverse non-logic expression
            # branches to make sure nested logical trees
            # are fixed too
            self.preorder(child)
            parent.append(child)

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
        flat_len = len(expr_node)
        # If we have simple single expr subnode,
        # just move contents of child to passed node
        if flat_len == 1:
            expr_node[:] = expr_node[0][:]
        # If there're just 3 children, process is
        # straight-forward - reform flat structure
        # into logical operation tree without any
        # additional analysis
        elif flat_len == 3:
            expr_lh, logic_node, expr_rh = expr_node
            del expr_node[:]
            expr_node.append(logic_node)
            logic_node.insert(0, expr_lh)
            logic_node.append(expr_rh)
        # When we have 5 or more elements in the flat structure,
        # we have to perform analysis on how to structurize tree
        else:
            token_map = self.get_token_map(expr_node)
            jumptargets = tuple(token_map.keys())
            # Assume we pick 1st logic operand for
            # division of list into tree with 2 branches
            pick_idx = 1
            for child_idx in range(len(expr_node)):
                child = expr_node[child_idx]
                # Skip all non-logic nodes
                if child.type not in ('and', 'or'):
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
            # Move logic node to its proper position,
            # split flat list into two parts, place both
            # into new expr nodes, and add these expr nodes
            # to logic node. Also run method on split flat
            # parts to ensure they're processed too.
            flat_lh = expr_node[:pick_idx]
            logic_node = expr_node[pick_idx]
            flat_rh = expr_node[pick_idx+1:]
            del expr_node[:]
            expr_node.append(logic_node)
            expr_lh = ASTNode('expr')
            expr_lh += flat_lh
            self.layout(expr_lh)
            logic_node.insert(0, expr_lh)
            expr_rh = ASTNode('expr')
            expr_rh += flat_rh
            self.layout(expr_rh)
            logic_node.append(expr_rh)

