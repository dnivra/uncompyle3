from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestMisc(BlackBoxTestCase):

    def test_builtin_call(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/globals.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/globals.py"
        self.assertProgramOutput(infile, expected)

    def test_builtin_call_dual(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/globals_locals.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/globals_locals.py"
        self.assertProgramOutput(infile, expected)

    def test_assign(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/assign.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/assign.py"
        self.assertProgramOutput(infile, expected)

    def test_assign_none(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/assign_none.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/assign_none.py"
        self.assertProgramOutput(infile, expected)

    def test_assign_none_str(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/assign_none_str.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/assign_none_str.py"
        self.assertProgramOutput(infile, expected)
