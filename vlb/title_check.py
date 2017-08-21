'''
check identifiers type 15, ISBN without hyphenation
get product id
get subtitle 
get title
get availability status code
get edition number, edition text
get contributors fullname for each contributor
get prices country, territory, currency, validFrom, value for each price
get mediaFiles count of list
'''
import sys
sys.path.append('C:\\Code\\trade_cat_scripts\\vlb\\lib')
from product import Product
from library import get_product, get_sheetdata
from openpyxl import Workbook
import time

startTime = time.time()

# data = get_product(9781430261063)
# data = get_product(9783476043306)
# book = Product(data)
# print(book.title)
# print(book.isbn)
# print(book.availability)
# print(book.prices)

# isbns = ['9781430261063', '9781484209264', '9781484211922', '9781484213933']

buk = Workbook()

outsheet = buk.active
outsheet.title = 'isbn check'

# name the output headers
# make this dynamic, or create in library
n_row_full = 1
outsheet.cell(row=n_row_full, column=1, value="BFLUX ISBN")
outsheet.cell(row=n_row_full, column=2, value="BFLUX Title")
outsheet.cell(row=n_row_full, column=3, value="VLB ISBN")
outsheet.cell(row=n_row_full, column=4, value="VLB Title")
outsheet.cell(row=n_row_full, column=5, value="ISBN Match")
# blfux relevant for promotion
# outsheet.cell(row=n_row_full, column=6, value="BLFUX Relevant for Promotion")
outsheet.cell(row=n_row_full, column=6, value="VLB Availability")
# price eur br
# outsheet.cell(row=n_row_full, column=8, value="price_eur_br")
outsheet.cell(row=n_row_full, column=7, value="# of VLB Prices")
outsheet.cell(row=n_row_full, column=8, value="Price DE")

data = get_sheetdata('dataset\dataset2017.xlsx')

count = data.max_row

for n in range(2, 100):
	print(n)
	isbn = data.cell(row=n, column=1).value
	n_row_full += 1
	product_data = get_product(isbn)
	book = Product(product_data)

	if isbn == book.isbn:
		match = True
	else:
		match = False		

	outsheet.cell(row=n_row_full, column=1, value=isbn)
	outsheet.cell(row=n_row_full, column=2, value=data.cell(row=n, column=2).value)
	outsheet.cell(row=n_row_full, column=3, value=book.isbn)
	outsheet.cell(row=n_row_full, column=4, value=book.title)
	outsheet.cell(row=n_row_full, column=5, value=match)
	outsheet.cell(row=n_row_full, column=6, value=book.availability)
	outsheet.cell(row=n_row_full, column=7, value=book.prices)
	outsheet.cell(row=n_row_full, column=8, value=book.price_DE)

buk.save('results\\vlb_data_delilah.xlsx')

print ('The script took {0} seconds !'.format(time.time() - startTime))