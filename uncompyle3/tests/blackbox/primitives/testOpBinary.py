from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestOpBinary(BlackBoxTestCase):

    def testAdd(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_add.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_add.py"
        self.assertProgramOutput(infile, expected)

    def testSubtract(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_subtract.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_subtract.py"
        self.assertProgramOutput(infile, expected)
