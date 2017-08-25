import unittest
import sys
# sys.path.append('C:\\Code\\trade_cat_scripts\\lib')
sys.path.append('..\\lib')
from bflux_item import BFLUXItem
from library_common import get_sheetdata

data = get_sheetdata('C:\\Code\\trade_cat_scripts\\tests\\dataset\\dataset2017.xlsx')
item = BFLUXItem(data, 12107)

class bfluxItemTests(unittest.TestCase):

	def test_properties(self):

		self.assertTrue(item.isbn == '9781137598936')
		self.assertTrue(item.title == 'Documentary and Disability')
		self.assertTrue(item.imprint == 'Palgrave Macmillan')
		self.assertTrue(item.price_DE == 96.29)
		self.assertTrue(item.price_AT == 98.99)
		self.assertTrue(item.price_CH == 99.00)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
