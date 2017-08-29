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

data = get_sheetdata('C:\\Code\\trade_cat_scripts\\tests\\dataset\\isbn_to_check.xlsx')
item = BFLUXItem(data, 2)

with open('dataset\\vlb_test_pickle.txt', 'rb') as content:
	product_data = pickle.load(content)

product = Product(product_data)

report = Report('isbn check', 'VLB')

report.generate(2, item, product)

report.save('test_report')

report_data = get_sheetdata('C:\\Code\\trade_cat_scripts\\tests\\test_report.xlsx')

class reportTests(unittest.TestCase):
	
	def testProperties(self):		
		self.assertTrue(report_data.cell(row=2, column=1).value == item.isbn)
		self.assertTrue(report_data.cell(row=2, column=2).value == item.title)
		self.assertTrue(report_data.cell(row=2, column=3).value == item.imprint)
		self.assertTrue(report_data.cell(row=2, column=4).value == product.isbn)
		self.assertTrue(report_data.cell(row=2, column=5).value == product.title)
		self.assertTrue(report_data.cell(row=2, column=6).value == True)
		self.assertTrue(report_data.cell(row=2, column=7).value == item.promo_status)
		self.assertTrue(report_data.cell(row=2, column=8).value == item.del_status)
		self.assertTrue(report_data.cell(row=2, column=9).value == product.availability)
		self.assertTrue(report_data.cell(row=2, column=10).value == product.availability_desc)
		self.assertTrue(report_data.cell(row=2, column=11).value == item.price_DE)
		self.assertTrue(report_data.cell(row=2, column=12).value == product.price_DE)
		self.assertTrue(report_data.cell(row=2, column=13).value == True)
		self.assertTrue(report_data.cell(row=2, column=14).value == item.price_AT)
		self.assertTrue(report_data.cell(row=2, column=15).value == product.price_AT)
		self.assertTrue(report_data.cell(row=2, column=16).value == True)
		self.assertTrue(report_data.cell(row=2, column=17).value == item.price_CH)
		self.assertTrue(report_data.cell(row=2, column=18).value == product.price_CH)
		self.assertTrue(report_data.cell(row=2, column=19).value == True)
		self.assertTrue(report_data.cell(row=2, column=20).value == product.prices)
		self.assertTrue(report_data.cell(row=2, column=21).value == product.front_cover)		
		self.assertTrue(report_data.cell(row=2, column=22).value == None)



		# pass
		

def main():
	unittest.main()

if __name__ == '__main__':
    main()