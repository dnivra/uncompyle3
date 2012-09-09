from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestPrecedence(BlackBoxTestCase):

    def test_structure(self):
        # Test case when precedences of whole expression
        # are the same, but expression structure differs from
        # 'flat' and it was structurized other way due to
        # parenthesis in source code
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/precedence/structure.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/precedence/structure.py"
        self.assertProgramOutput(infile, expected)

    def test_left(self):
        # Test case when precedences of whole expression
        # are the same, but expression structure differs from
        # 'flat' and it was structurized other way due to
        # parenthesis in source code
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/precedence/left.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/precedence/left.py"
        self.assertProgramOutput(infile, expected)

    def test_right(self):
        # Test case when precedences of whole expression
        # are the same, but expression structure differs from
        # 'flat' and it was structurized other way due to
        # parenthesis in source code
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/precedence/right.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/precedence/right.py"
        self.assertProgramOutput(infile, expected)
