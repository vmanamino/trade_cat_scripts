import unittest
import sys
sys.path.append('C:\\Code\\trade_cat_scripts\\vlb\\lib')
from library_vlb import dach_prices
import pickle

with open('dataset\\vlb_test_dach_prices_pickle.txt', 'rb') as content:
	vlb_prices = pickle.load(content)
vlb_prices = dach_prices(vlb_prices)

class dachPricesTests(unittest.TestCase):
	def testValidPrices(self):
		self.assertTrue(vlb_prices['DE'] == 123.04)
		self.assertTrue(vlb_prices['AT'] == 126.49)
		self.assertTrue(vlb_prices['CH'] == 126.5)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
