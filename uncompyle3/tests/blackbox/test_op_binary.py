from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestOpBinary(BlackBoxTestCase):

    def test_power(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/power.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/power.py"
        self.assertProgramOutput(infile, expected)

    def test_multiply(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/multiply.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/multiply.py"
        self.assertProgramOutput(infile, expected)

    def test_divide_floor(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/divide_floor.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/divide_floor.py"
        self.assertProgramOutput(infile, expected)

    def test_divide_true(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/divide_true.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/divide_true.py"
        self.assertProgramOutput(infile, expected)

    def test_modulo(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/modulo.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/modulo.py"
        self.assertProgramOutput(infile, expected)

    def test_add(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/add.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/add.py"
        self.assertProgramOutput(infile, expected)

    def test_subtract(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/subtract.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/subtract.py"
        self.assertProgramOutput(infile, expected)

    def test_subscription(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/subscription.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/subscription.py"
        self.assertProgramOutput(infile, expected)

    def test_shift_left(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/shift_left.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/shift_left.py"
        self.assertProgramOutput(infile, expected)

    def test_shift_right(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/shift_right.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/shift_right.py"
        self.assertProgramOutput(infile, expected)

    def test_and(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/and.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/and.py"
        self.assertProgramOutput(infile, expected)

    def test_xor(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/xor.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/xor.py"
        self.assertProgramOutput(infile, expected)

    def test_or(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/or.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_binary/or.py"
        self.assertProgramOutput(infile, expected)
