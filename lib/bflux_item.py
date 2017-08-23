from library_common import get_sheetdata

class BFLUXItem():

	def __init__(self, data, row_n):
		
		if row_n >= 2:
			self.isbn = data.cell(row=row_n, column=1).value
			self.title = data.cell(row=row_n, column=2).value
			self.copyright_year = data.cell(row=row_n, column=3).value
			self.medium = data.cell(row=row_n, column=4).value
			self.promo_status = data.cell(row=row_n, column=5).value
			self.price_DE = data.cell(row=row_n, column=6).value
		else:
			self.isbn = "no item provided"
			self.title = "no item provided"
			self.copyright_year = "no item provided"
			self.medium = "no item provided"
			self.promo_status = "no item provided"
			self.price_de = "no item provided"

# data = get_sheetdata('..\\vlb\dataset\dataset2017.xlsx')
# item = BFLUXItem(data, 1)
# print(item.isbn)
# print(item.title)
# print(item.copyright_year)
# print(item.medium)
# print(item.promo_status)
# print(item.price_de)
