import unittest
from tests import TestDefaults

def get_test_cases(test_folder):
	pass

if __name__ == "__main__":
	#TODO: make a function to get the list from tests directory (testcase object)
	testCases = [TestDefaults.TestDefaults]
	
	for testCase in testCases:
		suite = unittest.TestLoader().loadTestsFromTestCase(testCase)
		unittest.TextTestRunner(verbosity=2).run(suite)
