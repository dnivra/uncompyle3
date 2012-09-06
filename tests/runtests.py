import argparse
import os.path
import sys
import unittest

current_dir = os.path.dirname(__file__)
# Add Eos module to python paths
sys.path.append(os.path.realpath(os.path.join(current_dir, "..")))

if __name__ == "__main__":
    # Parse command line option (which is optional and positional)
    parser = argparse.ArgumentParser(description="Run uncompyle3 tests")
    parser.add_argument("suite", nargs='?', type=str, help="system or module path to test suite to run, defaults to all tests", default=".")
    args = parser.parse_args()
    # Get all tests into suite
    tests = unittest.TestLoader().discover(args.suite, "test*.py")
    # Run them
    unittest.TextTestRunner().run(tests)
