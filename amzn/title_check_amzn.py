import datetime
import hmac
import hashlib
import base64
from hashlib import sha256
import os
import sys
# append path to keys for import
sys.path.append('C:\\Code\\trade_cat_scripts')
import keys
from urllib.parse import urlencode, quote_plus


date_time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')

amzn_id = os.environ['AMZN_DE_ACCESS_ID']
amzn_key = os.environ['AMZN_DE_ACCESS_KEY']
amzn_key = bytes(amzn_key, 'utf-8' )
assoc_tag = os.environ['AMZN_ASSOC_TAG']

date_list = date_time.split(':')
print(date_list)
date_time_encoded = '%'.join(date_list)
print(date_time_encoded)

req = ('http://webservices.amazon.de/onca/xml?AWSAccessKeyId='+amzn_id+'&AssociateTag='+assoc_tag+'&ContentType'
'=&IdType=ISBN&ItemId=9781484219379&Operation=ItemLookup&ResponseGroup=Images&SearchIndex=Books&Service=AWSECommerceService&'
'Timestamp='+date_time_encoded)

my_list = req.split('&')
print(my_list)
my_list.sort()
print(my_list)
del my_list[0]
param_vals_bytes = []
count = 0

a = 'alphabet'
A = 'Alphabet'

# for each in my_list:
# 	count += 1
# 	data = bytes(each, 'ascii')
# 	if count is 1:
# 		param_vals_bytes.append(data)
# 	else:
# 		if param_vals_bytes


# print(my_list)

# my_list.sort()

# print(my_list)








# item_id = '9781484219379'

# payload = {'AWSAccessKeyId': amzn_id,
# 			'AssociateTag': assoc_tag,
# 			'IdType': 'ISBN',
# 			'ItemId': item_id,
# 			'Operation': 'ItemLookup',
# 			'ResponseGroup': 'Images',
# 			'SearchIndex': 'Books',
# 			'Service': 'AWSECCommerceService',
# 			'Timestamp': date_time}



# query = urlencode(payload, quote_via=quote_plus)

# data = "GET\nwebservices.amazon.de\n/onca/xml\n"+query

# data = urlencode(data)
# digest = hmac.new(amzn_key, data, sha256).digest()

# print(digest)
# req_as_bytes = str.encode(req)
# key_as_bytes = str.encode(amzn_key)

# dig = hmac.new(key_as_bytes, msg=req_as_bytes, digestmod=hashlib.sha256).digest()
# myhash = base64.b64encode(dig).decode()
# req = urllib.parse.quote(req)
# print(req)

# msg = bytes(req, 'utf-8')
# secret = bytes(amzn_key, 'utf-8')

# hash = hmac.new(secret, msg, hashlib.sha256)
# sig = base64.b64encode(hash.digest())


# print(sig)


# req += '&Signature='+str(sig)

# print(req)

# print(dig)

# print(myhash)

# print(req)