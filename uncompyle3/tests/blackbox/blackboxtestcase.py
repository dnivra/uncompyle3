import os
import re
from unittest import TestCase

from uncompyle3.uncompyle import Uncompyle


res_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'res')


class BlackBoxTestCase(TestCase):
    """
    Run whole application, providing input, and check
    output.
    """

    def assertProgramOutput(self, in_path, expected_path):
        infile = open(os.path.join(res_path, in_path), "rb")
        bytecode = infile.read()
        infile.close()
        expfile = open(os.path.join(res_path, expected_path), "r")
        expected = expfile.read()
        expfile.close()
        result = Uncompyle().run(bytecode)
        # Strip both actual and expected results from trailing newlines
        expected = re.sub("\n+$", "", expected)
        result = re.sub("\n+$", "", result)
        self.assertEqual(result, expected)
