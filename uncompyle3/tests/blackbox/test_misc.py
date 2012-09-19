from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestMisc(BlackBoxTestCase):

    def test_builtin_call(self):
        infile = "misc/globals.cpython-32.pyc"
        expected = "misc/globals.py"
        self.assertProgramOutput(infile, expected)

    def test_builtin_call_dual(self):
        infile = "misc/globals_locals.cpython-32.pyc"
        expected = "misc/globals_locals.py"
        self.assertProgramOutput(infile, expected)

    def test_assign(self):
        infile = "misc/assign.cpython-32.pyc"
        expected = "misc/assign.py"
        self.assertProgramOutput(infile, expected)

    def test_assign_none(self):
        infile = "misc/assign_none.cpython-32.pyc"
        expected = "misc/assign_none.py"
        self.assertProgramOutput(infile, expected)

    def test_assign_none_str(self):
        infile = "misc/assign_none_str.cpython-32.pyc"
        expected = "misc/assign_none_str.py"
        self.assertProgramOutput(infile, expected)

    def test_complex_script1(self):
        infile = "misc/complex_script1.cpython-32.pyc"
        expected = "misc/complex_script1.py"
        self.assertProgramOutput(infile, expected)

    def test_complex_script2(self):
        infile = "misc/complex_script2.cpython-32.pyc"
        expected = "misc/complex_script2.py"
        self.assertProgramOutput(infile, expected)
