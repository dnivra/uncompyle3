from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestComparison(BlackBoxTestCase):

    def test_equal(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/comparison/equal.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/comparison/equal.py"
        self.assertProgramOutput(infile, expected)

    def test_notqual(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/comparison/notequal.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/comparison/notequal.py"
        self.assertProgramOutput(infile, expected)

    def test_greater(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/comparison/greater.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/comparison/greater.py"
        self.assertProgramOutput(infile, expected)

    def test_greater_equal(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/comparison/greater_equal.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/comparison/greater_equal.py"
        self.assertProgramOutput(infile, expected)

    def test_less(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/comparison/less.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/comparison/less.py"
        self.assertProgramOutput(infile, expected)

    def test_less_equal(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/comparison/less_equal.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/comparison/less_equal.py"
        self.assertProgramOutput(infile, expected)

