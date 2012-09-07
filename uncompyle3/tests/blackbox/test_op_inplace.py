from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestOpInplace(BlackBoxTestCase):

    def test_power(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/power.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/power.py"
        self.assertProgramOutput(infile, expected)

    def test_multiply(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/multiply.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/multiply.py"
        self.assertProgramOutput(infile, expected)

    def test_divide_floor(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/divide_floor.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/divide_floor.py"
        self.assertProgramOutput(infile, expected)

    def test_divide_true(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/divide_true.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/divide_true.py"
        self.assertProgramOutput(infile, expected)

    def test_modulo(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/modulo.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/modulo.py"
        self.assertProgramOutput(infile, expected)

    def test_add(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/add.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/add.py"
        self.assertProgramOutput(infile, expected)

    def test_subtract(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/subtract.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/subtract.py"
        self.assertProgramOutput(infile, expected)

    def test_shift_left(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/shift_left.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/shift_left.py"
        self.assertProgramOutput(infile, expected)

    def test_shift_right(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/shift_right.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/shift_right.py"
        self.assertProgramOutput(infile, expected)

    def test_and(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/and.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/and.py"
        self.assertProgramOutput(infile, expected)

    def test_xor(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/xor.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/xor.py"
        self.assertProgramOutput(infile, expected)

    def test_or(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/or.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operations_inplace/or.py"
        self.assertProgramOutput(infile, expected)
