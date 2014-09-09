import os
import unittest


# TODO: find out how to retrieve test cases from a folder
def get_test_cases(test_folder):
    """Gets test cases from a folder

    Args:
            test_folder a folder where test_cases should be

    Returns:
            testcases that are in test_folder
    """
    # approximate plan:
    # 1. Check if file consists of classes
    # 2. Check if classes are of type unittest.TestCase
    # 3. if yes - append; else - move to the next class/file
    pass

if __name__ == "__main__":
    test_folder = os.path.abspath("tests")
    testCases = get_test_cases(test_folder)

    for testCase in testCases:
        suite = unittest.TestLoader().loadTestsFromTestCase(testCase)
        unittest.TextTestRunner(verbosity=2).run(suite)
