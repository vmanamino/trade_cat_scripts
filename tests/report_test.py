import pickle
import unittest
import sys
# sys.path.append('C:\\Code\\trade_cat_scripts\\lib')
sys.path.append('..\\lib')
from bflux_item import BFLUXItem
from library_common import get_sheetdata
from report import Report

sys.path.append('C:\\Code\\trade_cat_scripts\\vlb\\lib')
from product import Product

data = get_sheetdata('C:\\Code\\trade_cat_scripts\\tests\\dataset\\dataset2017.xlsx')
item = BFLUXItem(data, 12107)

with open('dataset\\vlb_test_pickle.txt', 'rb') as content:
	product_data = pickle.load(content)

product = Product(product_data)

report = Report('isbn check', 'VLB')

outsheet = report.generate(2, item, product)

class reportTests(unittest.TestCase):
	
	def testProperties(self):
		self.assertTrue(outsheet.cell(row=2, column=1) == item.isbn)
		self.assertTrue(outsheet.cell(row=2, column=2) == item.title)
		self.assertTrue(outsheet.cell(row=2, column=3) == item.imprint)
		self.assertTrue(outsheet.cell(row=2, column=4) == product.isbn)
		self.assertTrue(outsheet.cell(row=2, column=5) == product.title)
		self.assertTrue(outsheet.cell(row=2, column=1) == item.isbn)
