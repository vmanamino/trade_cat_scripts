from library import xlreport
from library import create_headers

class Report():
	
	
	
	def __init__(self, title, trader):

		outsheet = xlreport(title)
		report = create_headers(outsheet, trader)

		

