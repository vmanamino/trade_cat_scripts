from library_common import get_sheetdata

class BFLUXItem():

	def __init__(self, data, row_n):
		
		if row_n >= 2:
			self.isbn = data.cell(row=row_n, column=1).value
			self.title = data.cell(row=row_n, column=2).value
			self.imprint = data.cell(row=row_n, column=3).value 
			self.copyright_year = data.cell(row=row_n, column=4).value
			self.medium = data.cell(row=row_n, column=5).value
			self.promo_status = data.cell(row=row_n, column=6).value
			self.del_status = data.cell(row=row_n, column=7).value
			self.price_DE = data.cell(row=row_n, column=8).value
			self.price_AT = data.cell(row=row_n, column=9).value
			self.price_CH = data.cell(row=row_n, column=10).value
			self.cover_status = data.cell(row=row_n, column=11).value
		else:
			self.isbn = "no item provided"
			self.title = "no item provided"
			self.imprint = "no item provided"
			self.copyright_year = "no item provided"
			self.medium = "no item provided"
			self.promo_status = "no item provided"
			self.del_status = "no item provided"
			self.price_DE = "no item provided"
			self.price_AT = "no item provided"
			self.price_CH = "no item provided"
			self.cover_status = "no item provided"

# data = get_sheetdata('..\\vlb\dataset\dataset2017_prices.xlsx')
# item = BFLUXItem(data, 2)
# print(item.isbn)
# print(item.title)
# print(item.copyright_year)
# print(item.medium)
# print(item.promo_status)
# print(item.price_DE)
# print(item.price_AT)
# print(item.price_CH)

