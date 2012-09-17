from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestOpInplace(BlackBoxTestCase):

    def test_power(self):
        infile = "operation_inplace/power.cpython-32.pyc"
        expected = "operation_inplace/power.py"
        self.assertProgramOutput(infile, expected)

    def test_multiply(self):
        infile = "operation_inplace/multiply.cpython-32.pyc"
        expected = "operation_inplace/multiply.py"
        self.assertProgramOutput(infile, expected)

    def test_divide_floor(self):
        infile = "operation_inplace/divide_floor.cpython-32.pyc"
        expected = "operation_inplace/divide_floor.py"
        self.assertProgramOutput(infile, expected)

    def test_divide_true(self):
        infile = "operation_inplace/divide_true.cpython-32.pyc"
        expected = "operation_inplace/divide_true.py"
        self.assertProgramOutput(infile, expected)

    def test_modulo(self):
        infile = "operation_inplace/modulo.cpython-32.pyc"
        expected = "operation_inplace/modulo.py"
        self.assertProgramOutput(infile, expected)

    def test_add(self):
        infile = "operation_inplace/add.cpython-32.pyc"
        expected = "operation_inplace/add.py"
        self.assertProgramOutput(infile, expected)

    def test_subtract(self):
        infile = "operation_inplace/subtract.cpython-32.pyc"
        expected = "operation_inplace/subtract.py"
        self.assertProgramOutput(infile, expected)

    def test_shift_left(self):
        infile = "operation_inplace/shift_left.cpython-32.pyc"
        expected = "operation_inplace/shift_left.py"
        self.assertProgramOutput(infile, expected)

    def test_shift_right(self):
        infile = "operation_inplace/shift_right.cpython-32.pyc"
        expected = "operation_inplace/shift_right.py"
        self.assertProgramOutput(infile, expected)

    def test_and(self):
        infile = "operation_inplace/and.cpython-32.pyc"
        expected = "operation_inplace/and.py"
        self.assertProgramOutput(infile, expected)

    def test_xor(self):
        infile = "operation_inplace/xor.cpython-32.pyc"
        expected = "operation_inplace/xor.py"
        self.assertProgramOutput(infile, expected)

    def test_or(self):
        infile = "operation_inplace/or.cpython-32.pyc"
        expected = "operation_inplace/or.py"
        self.assertProgramOutput(infile, expected)
