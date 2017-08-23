import pickle
import unittest
import sys
sys.path.append('C:\\Code\\trade_cat_scripts\\vlb\\lib')
from product import Product


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
		
		# product isbn matches the isbn provided to the api
		self.assertTrue(product.isbn == '9783476043306')
		self.assertTrue(product_error.id == 401)
		self.assertTrue(product_error.title == '401')


def main():
    unittest.main()

if __name__ == '__main__':
    main()