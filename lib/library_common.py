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
	outsheet.cell(row=1, column=3, value="BFLUX Imprint")
	outsheet.cell(row=1, column=4, value=trader+" ISBN")
	outsheet.cell(row=1, column=5, value=trader+" Title")
	outsheet.cell(row=1, column=6, value="ISBN Match")
	outsheet.cell(row=1, column=7, value="BFLUX Promo Status")
	outsheet.cell(row=1, column=8, value="BFLUX Del Status")
	outsheet.cell(row=1, column=9, value=trader+" Availability")
	outsheet.cell(row=1, column=10, value="price_eur_br")
	outsheet.cell(row=1, column=11, value=trader+" Price DE")
	outsheet.cell(row=1, column=12, value="Price DE Match")
	outsheet.cell(row=1, column=13, value="price_eur_br_a")
	outsheet.cell(row=1, column=14, value=trader+" Price AT")
	outsheet.cell(row=1, column=15, value="Price AT Match")
	outsheet.cell(row=1, column=16, value="price_chf")
	outsheet.cell(row=1, column=17, value=trader+" Price CH")
	outsheet.cell(row=1, column=18, value="Price CH Match")
	outsheet.cell(row=1, column=19, value="# of "+trader+" Prices")
	outsheet.cell(row=1, column=20, value=trader+" Front Cover")
	outsheet.cell(row=1, column=21, value="BFLUX cover status")


	return outsheet

def add_row(outsheet, row_n, item, book):

	if item.isbn == book.isbn:
		match = True
	else:
		match = False		

	outsheet.cell(row=row_n, column=1, value=item.isbn)
	outsheet.cell(row=row_n, column=2, value=item.title)
	outsheet.cell(row=row_n, column=3, value=item.imprint)	
	outsheet.cell(row=row_n, column=4, value=book.isbn)
	outsheet.cell(row=row_n, column=5, value=book.title)
	outsheet.cell(row=row_n, column=6, value=match)
	outsheet.cell(row=row_n, column=7, value=item.promo_status)
	outsheet.cell(row=row_n, column=8, value=item.del_status)
	outsheet.cell(row=row_n, column=9, value=book.availability)
	outsheet.cell(row=row_n, column=10, value=item.price_DE)	
	outsheet.cell(row=row_n, column=11, value=book.price_DE)	

	if item.price_DE == book.price_DE:
		match = True
	else:
		match = False

	outsheet.cell(row=row_n, column=12, value=match)
	outsheet.cell(row=row_n, column=13, value=item.price_AT)
	outsheet.cell(row=row_n, column=14, value=book.price_AT)

	if item.price_AT == book.price_AT:
		match = True
	else:
		match = False

	outsheet.cell(row=row_n, column=15, value=match)
	outsheet.cell(row=row_n, column=16, value=item.price_CH)
	outsheet.cell(row=row_n, column=17, value=book.price_CH)

	if item.price_CH == book.price_CH:
		match = True
	else:
		match = False

	outsheet.cell(row=row_n, column=18, value=match)
	outsheet.cell(row=row_n, column=19, value=book.prices)
	outsheet.cell(row=row_n, column=20, value=book.front_cover)
	outsheet.cell(row=row_n, column=21, value=item.cover_status)

	
	return outsheet