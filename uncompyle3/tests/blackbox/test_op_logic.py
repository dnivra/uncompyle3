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
