import pickle
import unittest
import sys
sys.path.append('C:\\Code\\trade_cat_scripts\\vlb\\lib')
from product import Product
import json

with open('dataset\\vlb_test_pickle.txt', 'rb') as content:
	data = pickle.load(content)

product = Product(data)

with open('dataset\\vlb_test_pickle_error.txt', 'rb') as content:
	error = pickle.load(content)

product_error = Product(error)
# print(product.title)

class productDataTests(unittest.TestCase):

	def test_properties(self):

		self.assertTrue(product.title == 'Sparta Verfassungs- und Sozialgeschichte einer griechischen Polis')
		self.assertTrue(product.availability == 'MD')
		self.assertTrue(product.availability_desc == 'Manufactured on demand')
		
		# product isbn matches the isbn provided to the api
		self.assertTrue(product.isbn == '9783476043306')		
		self.assertTrue(product.price_DE == 29.99)
		self.assertTrue(product.price_AT == 30.83)
		self.assertTrue(product.price_CH == 31.0)
		self.assertTrue(product.front_cover == 'https://api.vlb.de/api/v1/cover/9783476043306/m')
		self.assertTrue(product_error.id == 401)
		self.assertTrue(product_error.title == '401')


def main():
    unittest.main()

if __name__ == '__main__':
    main()