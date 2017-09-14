####
class AmznProduct():

	def __init__(self, data):

		self.isbn = data['isbn']
		self.title = data['title_info']
		self.availability = data['availability']
		self.price = data['price_info']
		self.cover = data['cover_info']
