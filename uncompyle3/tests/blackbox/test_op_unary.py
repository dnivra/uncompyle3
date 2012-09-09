from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestOpUnary(BlackBoxTestCase):

    def test_positive(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_unary/positive.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_unary/positive.py"
        self.assertProgramOutput(infile, expected)

    def test_negative(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_unary/negative.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_unary/negative.py"
        self.assertProgramOutput(infile, expected)

    def test_not(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_unary/not.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_unary/not.py"
        self.assertProgramOutput(infile, expected)

    def test_invert(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_unary/invert.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_unary/invert.py"
        self.assertProgramOutput(infile, expected)

    def test_iter(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_unary/iter.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_unary/iter.py"
        self.assertProgramOutput(infile, expected)
