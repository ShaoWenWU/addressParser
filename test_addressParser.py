import unittest
import addressParser

class Test_addressParser(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		super(Test_addressParser, self).__init__()
    
	def runTest(self):
		self.test_addressParser()

	def  test_addressParser(self, inputAddress="Winterallee 3"):
		result = addressParser.addressParser(inputAddress)
		self.assertEqual(result, "{\"street\": \"Winterallee\", \"housenumber\": \"3\"}")

if __name__ == '__main__':
	unittest.main()