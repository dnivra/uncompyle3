import re
from unittest import TestCase

from uncompyle3.uncompyle import Uncompyle

# TODO: get rid of hardcoding throughout the blackbox tests

class BlackBoxTestCase(TestCase):
    """
    Run whole application, providing input, and check
    output.
    """

    def assertProgramOutput(self, in_path, expected_path):
        # TODO: add proper path detection
        infile = open(in_path, "rb")
        bytecode = infile.read()
        infile.close()
        expfile = open(expected_path, "r")
        expected = expfile.read()
        expfile.close()
        result = Uncompyle().run(bytecode)
        # Strip both actual and expected results from trailing newlines
        expected = re.sub("\n+$", "", expected)
        result = re.sub("\n+$", "", result)
        self.assertEqual(result, expected)
