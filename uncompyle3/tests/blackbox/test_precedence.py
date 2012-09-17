from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestPrecedence(BlackBoxTestCase):

    def test_structure(self):
        # Test case when precedences of whole expression
        # are the same, but expression structure differs from
        # 'flat' and it was structurized other way due to
        # parenthesis in source code
        infile = "precedence/structure.cpython-32.pyc"
        expected = "precedence/structure.py"
        self.assertProgramOutput(infile, expected)

    def test_left(self):
        # Test case when precedences of whole expression
        # are the same, but expression structure differs from
        # 'flat' and it was structurized other way due to
        # parenthesis in source code
        infile = "precedence/left.cpython-32.pyc"
        expected = "precedence/left.py"
        self.assertProgramOutput(infile, expected)

    def test_right(self):
        # Test case when precedences of whole expression
        # are the same, but expression structure differs from
        # 'flat' and it was structurized other way due to
        # parenthesis in source code
        infile = "precedence/right.cpython-32.pyc"
        expected = "precedence/right.py"
        self.assertProgramOutput(infile, expected)
