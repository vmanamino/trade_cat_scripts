from library import dach_prices

class Product():

	def __init__(self, data):
		
		self.response_code = data['code']
		product = data['content']
		
		try:
			if self.response_code == 200:				
				self.id = product['id']
				# code is from ONIX list 51	
				self.availability = product['availabilityStatusCode']
				# move this to library	
				if (len(product['titles']) >= 1):
					title = product['titles'][0]
					self.title = title['title']
					if title['subtitle']:
						self.title += ' '+title['subtitle']
				# move this to library
				for ident in product['identifiers']:
					if ident['type'] == '15':
						self.isbn = ident['value']
						break	
					else:
						self.isbn = 'not found'
				self.prices = len(product['prices'])
				self.price_DE = dach_prices(product['prices'])
				

			else:
				raise Exception

		except Exception as e:			
			self.id = self.response_code
			self.title = repr(self.response_code) + ' '+product['error']
			self.isbn = repr(self.response_code) + ' '+product['error']
			self.availability = repr(self.response_code) + ' '+product['error']

