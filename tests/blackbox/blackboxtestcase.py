import re
from subprocess import Popen, PIPE
from unittest import TestCase

# TODO: get rid of hardcoding throughout the blackbox tests

class BlackBoxTestCase(TestCase):
    """
    Run whole application, providing input, and check
    output.
    """

    def assertProgramOutput(self, bytecode_infile, expected_outfile):
        # TODO: add proper path detection
        process = Popen(["/home/dfx/src/uncompyle3/run.py", bytecode_infile], stdout=PIPE)
        stdout, stderr = process.communicate()
        self.assertIsNone(stderr, msg="stderr must be empty")
        exp_file = open(expected_outfile, "r")
        expected = exp_file.read()
        exp_file.close()
        actual_res = re.sub("\n+$", "", stdout.decode("utf8"))
        exp_res = re.sub("\n+$", "", expected)
        self.assertEqual(actual_res, exp_res, msg="stdout must match expected result")
