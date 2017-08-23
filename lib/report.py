from library import xlreport
from library import add_row
from library import create_headers


class Report():	
	
	def __init__(self, title, trader):

		self.workbook, self.name = xlreport(title)
		self.worksheet = self.workbook.active
		self.report = create_headers(self.worksheet, trader)

	def generate(self, row_n, item, book):
		# self.report = add_row(row_n, item, book)
		pass

	# @staticmethod
	def save(self, filename=None):
		if filename is None:
			filename = self.name
		filename += ".xlsx"
		self.workbook.save(filename)		
		print(filename)
			

data = get_sheetdata('..\\vlb\dataset\dataset2017.xlsx')	
report = Report('isbn check', 'VLB')
report.save()