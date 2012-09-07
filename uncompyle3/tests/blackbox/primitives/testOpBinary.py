from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestOpBinary(BlackBoxTestCase):

    def testPower(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_power.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_power.py"
        self.assertProgramOutput(infile, expected)

    def testMultiply(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_multiply.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_multiply.py"
        self.assertProgramOutput(infile, expected)

    def testFloorDivide(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_floordivide.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_floordivide.py"
        self.assertProgramOutput(infile, expected)

    def testTrueDivide(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_truedivide.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_truedivide.py"
        self.assertProgramOutput(infile, expected)

    def testModulo(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_modulo.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_modulo.py"
        self.assertProgramOutput(infile, expected)

    def testAdd(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_add.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_add.py"
        self.assertProgramOutput(infile, expected)

    def testSubtract(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_subtract.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_subtract.py"
        self.assertProgramOutput(infile, expected)

    def testSubscr(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_subscr.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_subscr.py"
        self.assertProgramOutput(infile, expected)

    def testLshift(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_lshift.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_lshift.py"
        self.assertProgramOutput(infile, expected)

    def testRshift(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_rshift.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_rshift.py"
        self.assertProgramOutput(infile, expected)

    def testAnd(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_and.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_and.py"
        self.assertProgramOutput(infile, expected)

    def testXor(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_xor.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_xor.py"
        self.assertProgramOutput(infile, expected)

    def testOr(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_or.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/op_bin_or.py"
        self.assertProgramOutput(infile, expected)
