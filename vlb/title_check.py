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
import time

startTime = time.time()
# product_data = get_product_data(9783662534991)
# product = Product(product_data)
# print(product_data)
# print(product.price_DE)
# print(product.availability_desc)


report = Report('isbn check', 'VLB')

data = get_sheetdata('dataset\dataset2017.xlsx')

count = data.max_row

for n in range(2, count):
	print(n)
	item = BFLUXItem(data, n)		
	product_data = get_product_data(item.isbn)
	book = Product(product_data)
	report.generate(n, item, book)

print_date = time.strftime("%d%m%y")
print_time = time.strftime("%I%M%S")

report.save('results\\vlb_isbn_check'+print_date+'_'+print_time)

print ('The script took {0} seconds !'.format(time.time() - startTime))