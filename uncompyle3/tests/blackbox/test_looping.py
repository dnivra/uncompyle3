from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestLooping(BlackBoxTestCase):

    def test_while(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/looping/while.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/looping/while.py"
        self.assertProgramOutput(infile, expected)
