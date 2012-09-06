from tests.blackbox.blackboxtestcase import BlackBoxTestCase


class TestCap(BlackBoxTestCase):
    """Test how capped attribute values are processed"""

    def testCapDefault(self):
        infile = "/home/dfx/src/uncompyle3/tests/blackbox/primitives/res/globals.cpython-32.pyc"
        expected = "/home/dfx/src/uncompyle3/tests/blackbox/primitives/res/globals.py"
        self.assertProgramOutput(infile, expected)
