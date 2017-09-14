import sys
sys.path.append('C:\\Code\\trade_cat_scripts\\amzn\\lib')
from library_amzn import collate_amzn_data as collate
from amzn_product import AmznProduct as Product

sys.path.append('C:\\Code\\trade_cat_scripts\\lib')
from library_common import get_sheetdata, get_worksheets
from bflux_item import BFLUXItem
from report import Report
import time
startTime = time.time()
# item_id = '9783476043306'
# data = collate(item_id)
# print(data)
# product = Product(data)
# print(product.isbn)

report = Report('isbn check', 'AmznDE')


medium = sys.argv[1]
promotion = sys.argv[2]
year = sys.argv[3]
option = sys.argv[4]

filename = medium + '_' + promotion + '_' + year + '.xlsx'
print(filename)

log_count = 0

log = open('results\\simple_log.txt', 'w')
log.write('%s\t%s\t%s\t%s\n' % ('Item logged', 'ISBN', 'Log time', 'Log date'))

if option == 'workbook':
	print(option)

	worksheets = get_worksheets('dataset\\'+filename)

	for data in worksheets:
		count = data.max_row
		# range is to, not including the upper limit
		count = count + 1
		for n in range(2, count):
			log_count += 1
			log_date = time.strftime("%d:%m:%y")
			log_time = time.strftime("%I:%M:%S")
			print(log_count, end=': ')
			print(log_time)		
			item = BFLUXItem(data, n)
			product_data = collate(item.isbn)			
			log.write('%s\t%s\t%s\t%s\n' % (log_count, item.isbn, log_time, log_date))
			book = Product(product_data)
			report.generate(n, item, book)

elif option == 'spreadsheet':
	print(option)
	data = get_sheetdata('dataset\\'+filename)
	count = data.max_row
	print(count)
	# range is to, not including the upper limit
	count = count + 1
	for n in range(2, 20):
		log_count += 1
		log_date = time.strftime("%d:%m:%y")
		log_time = time.strftime("%I:%M:%S")
		print(log_count, end=': ')
		print(log_time)		
		item = BFLUXItem(data, n)
		product_data = collate(item.isbn)		
		log.write('%s\t%s\t%s\t%s\n' % (log_count, item.isbn, log_time, log_date))
		book = Product(product_data)
		report.generate(n, item, book) 

print_date = time.strftime("%d%m%y")
print_time = time.strftime("%I%M%S")

report_name = 'vlb_'+medium + '_' + promotion + '_' + year + '_report_'+print_date+'_'+print_time
report.save('results\\'+report_name)
log.close()