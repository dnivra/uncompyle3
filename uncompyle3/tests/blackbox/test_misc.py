from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestMisc(BlackBoxTestCase):

    def testGlobalFunctionCall(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/globals.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/globals.py"
        self.assertProgramOutput(infile, expected)

    def testGlobalFunctionCallDual(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/globals_locals.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/globals_locals.py"
        self.assertProgramOutput(infile, expected)

    def testAssign(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/assign.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/assign.py"
        self.assertProgramOutput(infile, expected)

    def testAssignNone(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/assign_none.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/assign_none.py"
        self.assertProgramOutput(infile, expected)

    def testAssignNoneStr(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/assign_none_str.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/misc/assign_none_str.py"
        self.assertProgramOutput(infile, expected)
