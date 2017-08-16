import pickle
import unittest
import sys
sys.path.append('C:\\Code\\trade_cat_scripts\\vlb\\lib')
from product import Product


with open('dataset\\vlb_test_pickle.txt', 'rb') as content:
	data = pickle.load(content)

product = Product(data)
# print(product.title)

class productDataTests(unittest.TestCase):

	def test_properties(self):
		self.assertTrue(product.title == 'Sparta Verfassungs- und Sozialgeschichte einer griechischen Polis')


def main():
    unittest.main()

if __name__ == '__main__':
    main()