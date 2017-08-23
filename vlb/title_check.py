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
from library_vlb import get_product_data

sys.path.append('C:\\Code\\trade_cat_scripts\\lib')
from library_common import get_sheetdata
from bflux_item import BFLUXItem
from report import Report


from openpyxl import Workbook
import time

startTime = time.time()

# data = get_product_data(9781430261063)
# data = get_product_data(9783476043306)
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

report = Report('isbn check', 'VLB')

data = get_sheetdata('dataset\dataset2017.xlsx')

# count = data.max_row

for n in range(2, 1000):
	print(n)
	item = BFLUXItem(data, n)		
	product_data = get_product_data(item.isbn)
	book = Product(product_data)
	report.generate(n, item, book)

report.save('results\\vlb_data_delilah_test_2')

print ('The script took {0} seconds !'.format(time.time() - startTime))