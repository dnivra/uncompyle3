from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestCallArguments(BlackBoxTestCase):

    def test_positional(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/call_arguments/positional.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/call_arguments/positional.py"
        self.assertProgramOutput(infile, expected)
