import os
import unittest
import re


# Solution provided by http://stackoverflow.com/a/24562019
def get_test_cases(test_folder):
    """Gets test cases from a folder

    Args:
            test_folder a folder where test_cases should be

    Returns:
            testcases that are in test_folder
    """
    test_file_names = all_files_in(test_folder)
    return [path_to_module(str) for str in test_file_names]


def all_files_in(test_folder):
    matches = []
    for root, dirnames, filenames in os.walk(test_folder):
        for filename in filenames:
            if re.match(r"^Test.*.py$", filename):
                matches.append(os.path.join(root, filename))
    return matches


def path_to_module(filename):
    while filename.startswith('.'):
        filename = filename[1:]
    print filename.replace(".py", "").replace("\\", ".").replace("/", ".")
    return filename.replace(".py", "").replace("\\", ".").replace("/", ".")

if __name__ == "__main__":
    test_folder = "tests"
    test_names = get_test_cases(test_folder)
    test_suites = [unittest.defaultTestLoader.loadTestsFromName(
        suite_name) for suite_name in test_names]

    test_suite = unittest.TestSuite(test_suites)
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(test_suite)
