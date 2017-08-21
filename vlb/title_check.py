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
from library import get_product

sys.path.append('C:\\Code\\trade_cat_scripts\\lib')
from library import get_sheetdata
from bflux_item import BFLUXItem

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
outsheet.cell(row=n_row_full, column=6, value="BFLUX Promo Status")
outsheet.cell(row=n_row_full, column=7, value="VLB Availability")
outsheet.cell(row=n_row_full, column=8, value="price_eur_br")
outsheet.cell(row=n_row_full, column=9, value="Price DE")
outsheet.cell(row=n_row_full, column=10, value="Price Match")
outsheet.cell(row=n_row_full, column=11, value="# of VLB Prices")

data = get_sheetdata('dataset\dataset2017.xlsx')

count = data.max_row

for n in range(2, 1000):
	print(n)
	item = BFLUXItem(data, n)	
	n_row_full += 1 # change this to n
	product_data = get_product(item.isbn)
	book = Product(product_data)

	if item.isbn == book.isbn:
		match = True
	else:
		match = False		

	outsheet.cell(row=n_row_full, column=1, value=item.isbn)
	outsheet.cell(row=n_row_full, column=2, value=item.title)	
	outsheet.cell(row=n_row_full, column=3, value=book.isbn)
	outsheet.cell(row=n_row_full, column=4, value=book.title)
	outsheet.cell(row=n_row_full, column=5, value=match)
	outsheet.cell(row=n_row_full, column=6, value=item.promo_status)
	outsheet.cell(row=n_row_full, column=7, value=book.availability)
	outsheet.cell(row=n_row_full, column=8, value=item.price_DE)	
	outsheet.cell(row=n_row_full, column=9, value=book.price_DE)

	if item.price_DE == book.price_DE:
		match = True
	else:
		match = False

	outsheet.cell(row=n_row_full, column=10, value=match)
	outsheet.cell(row=n_row_full, column=11, value=book.prices)

buk.save('results\\vlb_data_delilah.xlsx')

print ('The script took {0} seconds !'.format(time.time() - startTime))