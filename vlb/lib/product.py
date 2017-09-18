from library_vlb import dach_prices, get_frontcover, avail_code_desc
import json

class Product():

	def __init__(self, data):
		
		self.response_code = data['code']
		product = content = json.loads(data['content'])
		
		if self.response_code == 200:				
			self.id = product['id']
			# code is from ONIX list 54	
			self.availability = product['availabilityStatusCode']
			self.availability_desc = avail_code_desc(self.availability)
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
			if len(product['prices']):
				self.prices = len(product['prices'])
			else:
				self.prices = 'None'
			dachs = dach_prices(product['prices'])
			self.price_DE = dachs['DE']
			self.price_AT = dachs['AT']
			self.price_CH = dachs['CH']
			# self.price_DE = dach_prices(product['prices'])
			self.front_cover = get_frontcover(product['mediaFiles'])
			

		else:			
			self.id = self.response_code
			self.title = repr(self.response_code)
			self.isbn = repr(self.response_code)
			self.availability = repr(self.response_code)
			self.availability_desc = repr(self.response_code)
			self.prices = repr(self.response_code)
			self.price_DE = repr(self.response_code)
			self.price_AT = repr(self.response_code)
			self.price_CH = repr(self.response_code)
			self.front_cover = repr(self.response_code)

