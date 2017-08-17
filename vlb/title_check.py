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
from openpyxl import Workbook

data = get_product(9781430261063)
book = Product(data)
print(book.title)
print(book.isbn)
print(book.availability)

# isbns = ['9781430261063', '9781484209264', '9781484211922', '9781484213933']

# buk = Workbook()

# outsheet = buk.active
# outsheet.title = 'isbn check'

# # name the output headers
# # make this dynamic
# n_row_full = 1
# outsheet.cell(row=n_row_full, column=1, value="BFLUX ISBN")
# outsheet.cell(row=n_row_full, column=2, value="BFLUX Title")
# outsheet.cell(row=n_row_full, column=3, value="VLB ISBN")
# outsheet.cell(row=n_row_full, column=4, value="VLB Title")
# outsheet.cell(row=n_row_full, column=5, value="ISBN Match")
# outsheet.cell(row=n_row_full, column=6, value="VLB Availability")

# for isbn in isbns:
# 	n_row_full += 1
# 	data = get_product(isbn)
# 	book = Product(data)

# 	if isbn == book.isbn:
# 		match = True
# 	else:
# 		match = False		

# 	outsheet.cell(row=n_row_full, column=1, value=isbn)
# 	outsheet.cell(row=n_row_full, column=3, value=book.isbn)
# 	outsheet.cell(row=n_row_full, column=4, value=book.title)
# 	outsheet.cell(row=n_row_full, column=5, value=match)
# 	outsheet.cell(row=n_row_full, column=6, value=book.availability)


# buk.save('vlb_data.xlsx')