from openpyxl import Workbook
from openpyxl import load_workbook

def get_sheetdata(file):

	wb = load_workbook(file)
	names = wb.get_sheet_names()
	return wb[names[0]] # data returned

def xlreport(title):

	buk = Workbook()
	outsheet = buk.active
	outsheet.title = title
	return buk, title

def create_headers(outsheet, trader):

	outsheet.cell(row=1, column=1, value="BFLUX ISBN")
	outsheet.cell(row=1, column=2, value="BFLUX Title")
	outsheet.cell(row=1, column=3, value=trader+" ISBN")
	outsheet.cell(row=1, column=4, value=trader+" Title")
	outsheet.cell(row=1, column=5, value="ISBN Match")
	outsheet.cell(row=1, column=6, value="BFLUX Promo Status")
	outsheet.cell(row=1, column=7, value=trader+" Availability")
	outsheet.cell(row=1, column=8, value="price_eur_br")
	outsheet.cell(row=1, column=9, value="Price DE")
	outsheet.cell(row=1, column=10, value="Price Match")
	outsheet.cell(row=1, column=11, value="# of "+trader+" Prices")
	outsheet.cell(row=1, column=12, value="# of "+trader+" Front Cover")

	return outsheet

def add_row(outsheet, row_n, item, book):

	if item.isbn == book.isbn:
		match = True
	else:
		match = False		

	outsheet.cell(row=row_n, column=1, value=item.isbn)
	outsheet.cell(row=row_n, column=2, value=item.title)	
	outsheet.cell(row=row_n, column=3, value=book.isbn)
	outsheet.cell(row=row_n, column=4, value=book.title)
	outsheet.cell(row=row_n, column=5, value=match)
	outsheet.cell(row=row_n, column=6, value=item.promo_status)
	outsheet.cell(row=row_n, column=7, value=book.availability)
	outsheet.cell(row=row_n, column=8, value=item.price_DE)	
	outsheet.cell(row=row_n, column=9, value=book.price_DE)	

	if item.price_DE == book.price_DE:
		match = True
	else:
		match = False

	outsheet.cell(row=row_n, column=10, value=match)
	outsheet.cell(row=row_n, column=11, value=book.prices)
	outsheet.cell(row=row_n, column=12, value=book.front_cover)


	pass