import sys
sys.path.append('C:\\Code\\trade_cat_scripts\\vlb\\lib')
from product import Product
from library_vlb import get_product_data

product = Product(get_product_data('9783540356455'))

