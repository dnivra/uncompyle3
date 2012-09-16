from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestOpLogic(BlackBoxTestCase):

    def test_and(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/and.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/and.py"
        self.assertProgramOutput(infile, expected)

    def test_or(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/or.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/or.py"
        self.assertProgramOutput(infile, expected)

    def test_and_complex1(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/complex1.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/complex1.py"
        self.assertProgramOutput(infile, expected)

    def test_and_complex2(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/complex2.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/complex2.py"
        self.assertProgramOutput(infile, expected)

    def test_and_complex3(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/complex3.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/complex3.py"
        self.assertProgramOutput(infile, expected)

    def test_and_complex4(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/complex4.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/complex4.py"
        self.assertProgramOutput(infile, expected)

    def test_and_complex5(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/complex5.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/complex5.py"
        self.assertProgramOutput(infile, expected)

    def test_and_complex6(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/complex6.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/complex6.py"
        self.assertProgramOutput(infile, expected)

    def test_and_complex7(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/complex7.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/complex7.py"
        self.assertProgramOutput(infile, expected)

    def test_and_complex8(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/complex8.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/complex8.py"
        self.assertProgramOutput(infile, expected)

    def test_and_complex9(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/complex9.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/complex9.py"
        self.assertProgramOutput(infile, expected)


