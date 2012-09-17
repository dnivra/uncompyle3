from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestCallArguments(BlackBoxTestCase):

    def test_positional(self):
        infile = "call_arguments/positional.cpython-32.pyc"
        expected = "call_arguments/positional.py"
        self.assertProgramOutput(infile, expected)

    def test_keyword(self):
        infile = "call_arguments/keyword.cpython-32.pyc"
        expected = "call_arguments/keyword.py"
        self.assertProgramOutput(infile, expected)
