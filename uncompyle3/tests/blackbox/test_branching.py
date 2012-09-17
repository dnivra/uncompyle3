from uncompyle3.tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestBranching(BlackBoxTestCase):

    def test_if(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/branching/if.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/branching/if.py"
        self.assertProgramOutput(infile, expected)

    def test_ifelse(self):
        infile = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/branching/ifelse.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/uncompyle3/tests/blackbox/res/branching/ifelse.py"
        self.assertProgramOutput(infile, expected)
