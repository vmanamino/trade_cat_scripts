

class Product():

	def __init__(self, data):
		
		self.response_code = data['code']
		
		try:
			if self.response_code == 200:
				product = data['content']
				self.id = product['id']				
				if (len(product['titles']) == 1):
					title = product['titles'][0]
					self.title = title['title']
					if title['subtitle']:
						self.title += ' '+title['subtitle']
				for ident in product['identifiers']:
					if ident['type'] == '15':
						self.isbn = ident['value']
						break				
			else:
				raise Exception

		except Exception as e:
			self.id = self.response_code
			self.title = repr(self.response_code) + ' '+product['content']['error']


