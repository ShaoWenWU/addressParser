import unittest
import addressParser
import csv
import pandas as pd
from ddt import ddt,data,unpack

def importTestCase(file_name):
	# df = pd.read_csv(file_name)
	# print("Imported test cases: ")
	# print(df)
	# inputData = df['Input'].values
	# expectedData = df['Expected'].values
	# data = []
	# data.append(inputData)
	# data.append(expectedData)
	# print("data: ", data)
	# return data
	rows=[]
	with open(file_name) as f:
		readers = csv.reader(f)
		for row in readers:
			rows.append(row)
	print("rows:", rows[1:])
	return rows[1:]


@ddt
class Test_addressParser(unittest.TestCase):

	# def __init__(self, *args, **kwargs):
	# 	super(Test_addressParser, self).__init__()
	def setUp(self):
		pass
	
	# def runTest(self):
	# 	self.test_addressParser()
	

	@data(*importTestCase('testCase.csv'))
	@unpack
	def test_addressParser(self, inputAddress, expected):
		result = addressParser.addressParser(inputAddress)
		# self.assertEqual(result, "{\"street\": \"Winterallee\", \"housenumber\": \"3\"}")
		self.assertEqual(result, expected)



if __name__ == '__main__':
	# unittest.main()
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_addressParser)
	unittest.TextTestRunner(verbosity=2).run(suite)
