from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestPrimitives(BlackBoxTestCase):

    def testGlobalFunctionCall(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/globals.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/globals.py"
        self.assertProgramOutput(infile, expected)

    def testGlobalFunctionCallDual(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/globals_locals.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/globals_locals.py"
        self.assertProgramOutput(infile, expected)

    def testAssign(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/assign.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/primitives/res/assign.py"
        self.assertProgramOutput(infile, expected)
