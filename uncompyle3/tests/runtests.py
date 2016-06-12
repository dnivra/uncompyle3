import argparse
import os.path
import sys
import unittest


script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.realpath(os.path.join(script_dir, '..', '..')))

if __name__ == '__main__':

    if sys.version_info.major != 3 or sys.version_info.minor < 3:
        sys.stderr.write('Tests require at least python 3.3 to run\n')
        sys.exit()

    # Parse command line option (which is optional and positional)
    parser = argparse.ArgumentParser(description='Run Eos tests')
    parser.add_argument(
        'suite', nargs='?', type=str,
        help='system path to test suite to run, defaults to all tests',
        default=script_dir
    )
    args = parser.parse_args()

    # If we have full path to file, adjust pattern so that we execute
    # tests only from that specific file
    suite_path = os.path.expanduser(args.suite)
    if os.path.isfile(suite_path):
        suite, pattern = os.path.split(suite_path)
    else:
        suite = suite_path
        pattern = 'test_*.py'

    # Get all tests into suite
    tests = unittest.TestLoader().discover(suite, pattern=pattern)
    # Run them
    unittest.TextTestRunner().run(tests)
