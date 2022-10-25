import unittest
from testproject.tests import tests

def run_tests():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(tests)

    with open("test_report.txt", "w") as logfile:
        runner = unittest.TextTestRunner(logfile, verbosity=3)
        res = runner.run(suite)

    print(f"{res.testsRun} tests run, {len(res.failures)} failures, {len(res.errors)} errors.")

if __name__ == "__main__":
    run_tests()