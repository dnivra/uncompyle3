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

    # In some more complex situations, different  opcodes
    # are used for logical operators, following tests check
    # alternative ones
    def test_and_alt(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/and_alt.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/and_alt.py"
        self.assertProgramOutput(infile, expected)

    def test_or_alt(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/or_alt.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/operation_logic/or_alt.py"
        self.assertProgramOutput(infile, expected)
