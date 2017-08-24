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
report = Report('isbn check', 'VLB')

data = get_sheetdata('dataset\dataset2017_imprints.xlsx')

# count = data.max_row

for n in range(2, 100):
	print(n)
	item = BFLUXItem(data, n)		
	product_data = get_product_data(item.isbn)
	book = Product(product_data)
	report.generate(n, item, book)

report.save('results\\vlb_data_delilah_test_imprints')

print ('The script took {0} seconds !'.format(time.time() - startTime))