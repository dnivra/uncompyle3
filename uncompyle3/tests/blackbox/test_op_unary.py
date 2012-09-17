from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestOpUnary(BlackBoxTestCase):

    def test_positive(self):
        infile = "operation_unary/positive.cpython-32.pyc"
        expected = "operation_unary/positive.py"
        self.assertProgramOutput(infile, expected)

    def test_negative(self):
        infile = "operation_unary/negative.cpython-32.pyc"
        expected = "operation_unary/negative.py"
        self.assertProgramOutput(infile, expected)

    def test_not(self):
        infile = "operation_unary/not.cpython-32.pyc"
        expected = "operation_unary/not.py"
        self.assertProgramOutput(infile, expected)

    def test_invert(self):
        infile = "operation_unary/invert.cpython-32.pyc"
        expected = "operation_unary/invert.py"
        self.assertProgramOutput(infile, expected)

    def test_iter(self):
        infile = "operation_unary/iter.cpython-32.pyc"
        expected = "operation_unary/iter.py"
        self.assertProgramOutput(infile, expected)
