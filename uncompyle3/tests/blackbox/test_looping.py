from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestLooping(BlackBoxTestCase):

    def test_while(self):
        infile = "looping/while.cpython-32.pyc"
        expected = "looping/while.py"
        self.assertProgramOutput(infile, expected)

    def test_for(self):
        infile = "looping/for.cpython-32.pyc"
        expected = "looping/for.py"
        self.assertProgramOutput(infile, expected)
