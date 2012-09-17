from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestOpBinary(BlackBoxTestCase):

    def test_power(self):
        infile = "operation_binary/power.cpython-32.pyc"
        expected = "operation_binary/power.py"
        self.assertProgramOutput(infile, expected)

    def test_multiply(self):
        infile = "operation_binary/multiply.cpython-32.pyc"
        expected = "operation_binary/multiply.py"
        self.assertProgramOutput(infile, expected)

    def test_divide_floor(self):
        infile = "operation_binary/divide_floor.cpython-32.pyc"
        expected = "operation_binary/divide_floor.py"
        self.assertProgramOutput(infile, expected)

    def test_divide_true(self):
        infile = "operation_binary/divide_true.cpython-32.pyc"
        expected = "operation_binary/divide_true.py"
        self.assertProgramOutput(infile, expected)

    def test_modulo(self):
        infile = "operation_binary/modulo.cpython-32.pyc"
        expected = "operation_binary/modulo.py"
        self.assertProgramOutput(infile, expected)

    def test_add(self):
        infile = "operation_binary/add.cpython-32.pyc"
        expected = "operation_binary/add.py"
        self.assertProgramOutput(infile, expected)

    def test_subtract(self):
        infile = "operation_binary/subtract.cpython-32.pyc"
        expected = "operation_binary/subtract.py"
        self.assertProgramOutput(infile, expected)

    def test_subscription(self):
        infile = "operation_binary/subscription.cpython-32.pyc"
        expected = "operation_binary/subscription.py"
        self.assertProgramOutput(infile, expected)

    def test_shift_left(self):
        infile = "operation_binary/shift_left.cpython-32.pyc"
        expected = "operation_binary/shift_left.py"
        self.assertProgramOutput(infile, expected)

    def test_shift_right(self):
        infile = "operation_binary/shift_right.cpython-32.pyc"
        expected = "operation_binary/shift_right.py"
        self.assertProgramOutput(infile, expected)

    def test_and(self):
        infile = "operation_binary/and.cpython-32.pyc"
        expected = "operation_binary/and.py"
        self.assertProgramOutput(infile, expected)

    def test_xor(self):
        infile = "operation_binary/xor.cpython-32.pyc"
        expected = "operation_binary/xor.py"
        self.assertProgramOutput(infile, expected)

    def test_or(self):
        infile = "operation_binary/or.cpython-32.pyc"
        expected = "operation_binary/or.py"
        self.assertProgramOutput(infile, expected)
