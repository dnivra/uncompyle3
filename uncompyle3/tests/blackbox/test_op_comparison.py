from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestOpComparison(BlackBoxTestCase):

    def test_equal(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_comparison/equal.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_comparison/equal.py"
        self.assertProgramOutput(infile, expected)

    def test_notqual(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_comparison/notequal.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_comparison/notequal.py"
        self.assertProgramOutput(infile, expected)

    def test_greater(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_comparison/greater.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_comparison/greater.py"
        self.assertProgramOutput(infile, expected)

    def test_greater_equal(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_comparison/greater_equal.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_comparison/greater_equal.py"
        self.assertProgramOutput(infile, expected)

    def test_less(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_comparison/less.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_comparison/less.py"
        self.assertProgramOutput(infile, expected)

    def test_less_equal(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_comparison/less_equal.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_comparison/less_equal.py"
        self.assertProgramOutput(infile, expected)

