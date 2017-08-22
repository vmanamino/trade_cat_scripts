from library import xlreport
from library import add_row
from library import create_headers

class Report():	
	
	def __init__(self, title, trader):

		outsheet = xlreport(title)
		self.report = create_headers(outsheet, trader)

	def generate(self, row_n, item, book):
		# self.report = add_row(row_n, item, book)
		pass

	@staticmethod
	def save(filename):
		outsheet.save(filename)
			# pass
		

report = Report('isbn check', 'VLB')
report.save('test.xslx')