import sys
sys.path.append('C:\\Code\\trade_cat_scripts\\vlb\\lib')
from product import Product
from library_vlb import get_product_data

from library_common import xlreport
from library_common import create_headers
from library_common import get_sheetdata
from library_common import add_row
from bflux_item import BFLUXItem

class Report():	
	
	def __init__(self, title, trader):

		self.workbook, self.name = xlreport(title)
		self.worksheet = self.workbook.active
		self.report = create_headers(self.worksheet, trader)

	def generate(self, row_n, item, book):
		self.report = add_row(self.worksheet, row_n, item, book)
		# pass

	# @staticmethod
	def save(self, filename=None):

		# add something to handle the directory
		# force the xlsx extension for gitignoring
		if filename is None:
			filename = self.name
		filename += ".xlsx"
		self.workbook.save(filename)		
		print(filename)
			
# data = get_product_data(9783476043306)
# book = Product(data)
# data = get_sheetdata('..\\vlb\dataset\dataset2017.xlsx')
# item = BFLUXItem(data, 2)
# report = Report('isbn check', 'VLB')
# report.generate(2, item, book)
# report.save()