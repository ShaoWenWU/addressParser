import unittest
import addressParser
import csv
from ddt import ddt,data,unpack
import HtmlTestRunner

def importTestCase(file_name):
	rows=[]
	with open(file_name) as f:
		readers = csv.DictReader(f, delimiter=',')
		for row in readers:
			rows.append([row['Input'], row['Expected']])
	print("Imported DATA: \n", rows, "\n")
	return rows


@ddt
class Test_addressParser(unittest.TestCase):

	def setUp(self):
		pass
	
	@data(*importTestCase('testCase.csv'))
	@unpack
	def test_addressParser(self, inputAddress, expected):
		result = addressParser.addressParser(inputAddress)
		self.assertEqual(result, expected)



if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_addressParser)

	runner = HtmlTestRunner.HTMLTestRunner(
				verbosity=1,
				report_title='Test Report',
				descriptions='Test report of multiple input cases.'
                )

	runner.run(suite)
