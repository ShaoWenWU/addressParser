import unittest
import addressParser
import csv
from ddt import ddt, data, unpack
import HtmlTestRunner
import pycodestyle


def importTestCase(file_name):
    rows = []
    with open(file_name, encoding='utf-8-sig') as f:
        readers = csv.DictReader(f, delimiter=',')
        for row in readers:
            rows.append([row['Input'], row['Expected']])
    print("Imported DATA: ", file_name, "\n")
    return rows


@ddt
class Test_addressParser(unittest.TestCase):

    def setUp(self):
        # self.path = ['.', ]  # Check all file within current project
        self.path = ['addressParser.py', 'test_addressParser.py']
        # pass

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(self.path)
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

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
