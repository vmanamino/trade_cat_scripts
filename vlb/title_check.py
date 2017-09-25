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
from library_vlb import get_worksheets

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


medium = sys.argv[1]
promotion = sys.argv[2]
year = sys.argv[3]
option = sys.argv[4]

filename = medium + '_' + promotion + '_' + year + '.xlsx'
print(filename)

log_count = 0

print_date = time.strftime("%d%m%y")
print_time = time.strftime("%I%M%S")

log = open('results\\'+medium+'_simple_log_'+print_date+'_'+print_time+'.txt', 'w')
log.write('%s\t%s\t%s\t%s\t%s\n' % ('Item logged', 'Code', 'ISBN', 'Log time', 'Log date'))

if option == 'workbook':
	print(option)

	# total item count continually added to, start at one for the report header
	item_count = 1

	worksheets = get_worksheets('dataset\\'+filename)

	for data in worksheets:
		count = data.max_row
		
		# range is to, not including the upper limit
		count = count + 1

		for n in range(2, count):
			log_count += 1
			item_count += 1
			log_date = time.strftime("%d:%m:%y")
			log_time = time.strftime("%I:%M:%S")
			print(log_count, end=': ')
			print(log_time)		
			item = BFLUXItem(data, n)
			product_data = get_product_data(item.isbn)
			print(product_data['code'])
			log.write('%s\t%s\t%s\t%s\t%s\n' % (log_count, product_data['code'], item.isbn, log_time, log_date))
			book = Product(product_data)
			report.generate(item_count, item, book)

		print(item_count)

elif option == 'spreadsheet':
	print(option)
	data = get_sheetdata('dataset\\'+filename)
	count = data.max_row
	print(count)
	# range is to, not including the upper limit
	count = count + 1
	for n in range(2, count):
		log_count += 1
		log_date = time.strftime("%d:%m:%y")
		log_time = time.strftime("%I:%M:%S")
		print(log_count, end=': ')
		print(log_time)		
		item = BFLUXItem(data, n)
		product_data = get_product_data(item.isbn)
		print(product_data['code'])
		log.write('%s\t%s\t%s\t%s\n' % (log_count, product_data['code'], log_time, log_date))
		book = Product(product_data)
		report.generate(n, item, book) 

print_date = time.strftime("%d%m%y")
print_time = time.strftime("%I%M%S")

report_name = 'vlb_'+medium + '_' + promotion + '_' + year + '_report_'+print_date+'_'+print_time
report.save('results\\'+report_name)
log.close()

print ('The script took {0} seconds !'.format(time.time() - startTime))