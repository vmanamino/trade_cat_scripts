import datetime
# import time
import hmac
import hashlib
import base64
from hashlib import sha256
import os
import sys
# append path to keys for import
sys.path.append('C:\\Code\\trade_cat_scripts')
import keys
import urllib
import urllib.request
from urllib.parse import urlencode, quote_plus
from xml.etree import cElementTree as xmlDoc

sys.path.append('C:\\Code\\trade_cat_scripts\\lib')
# from library_common import response_dict


# set these parameter for future development
id_type = 'ISBN'
item_id = '9783476043306'
operation = 'ItemLookup'
responseGroup = 'OfferSummary'
searchIndex = 'Books'

def get_amzn_request(url):

    request = urllib.request.Request(url)
    try:
    	return urllib.request.urlopen(request)
    except urllib.request.HTTPError as err:
    	return err


def get_amzn_product_data(isbn, data_point):

	s = create_string(isbn, data_point)
	pairs = create_pairs(s)
	s_to_send = create_prefixes(pairs)
	digest = create_digest(s_to_send)
	signature_param_value = create_signature(digest)
	url = create_autographed_url(s_to_send, signature_param_value)
	return url
	# return get_amzn_request(url)

def create_string(item_id,  responseGroup, id_type='ISBN', operation='ItemLookup', searchIndex='Books'):
	amzn_id = os.environ['AMZN_DE_ACCESS_ID']
	assoc_tag = os.environ['AMZN_ASSOC_TAG']

	# create timestamp
	date_time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')

	date_time = urllib.parse.quote(date_time, safe='')
	print(date_time)
	
	s = ('http://webservices.amazon.de/onca/xml?AWSAccessKeyId='+amzn_id+'&AssociateTag='+assoc_tag+'&'
	'IdType='+id_type+'&ItemId='+item_id+'&Operation='+operation+'&ResponseGroup='+responseGroup+'&SearchIndex='+searchIndex+'&Service=AWSECommerceService&'
	'Timestamp='+date_time)
	
	return s

# s = create_string(item_id, responseGroup) # ok

def create_pairs(s):

	# break string into pairs of param and value
	pairs = s.split('?')
	del pairs[0]
	pairs = pairs[0].split('&')

	# sort the pairs based on binary values
	pairs.sort()

	# join pairs again into a string
	s = "&".join(pairs)

	return s

# pairs = create_pairs(s) # ok

def create_prefixes(s):
	# begin building the request
	verb = 'GET\n'
	domain = 'webservices.amazon.de\n'
	expression = '/onca/xml\n'
	to_be_prepended = verb + domain + expression
	s_to_send = to_be_prepended + s

	return s_to_send

# s_to_send = create_prefixes(pairs) # ok

def create_digest(s_to_send):
	amzn_key = os.environ['AMZN_DE_ACCESS_KEY']
	s_to_send = bytes(s_to_send, 'utf-8')
	amzn_key = bytes(amzn_key, 'utf-8')
	digest = hmac.new(amzn_key, msg=s_to_send, digestmod=hashlib.sha256).digest()

	return digest

# digest = create_digest(s_to_send) # ok

def create_signature(digest):

	signature = base64.b64encode(digest)
	signature_string = signature.decode('utf-8')
	signature_url_encoded = urllib.parse.quote(signature_string, safe='')
	signature_param_value = '&Signature='+signature_url_encoded

	return signature_param_value

# signature_param_value = create_signature(digest) # ok

def create_autographed_url(s_to_send, signature_param_value):

	s_as_stanza = s_to_send+''+signature_param_value
	s_verb_removed = s_as_stanza[4:]
	request = s_verb_removed.replace('\n', '').replace('xml', 'xml?')
	http_prefix = 'http://'
	url_request = http_prefix + request

	return url_request

# url = create_autographed_url(s_to_send, signature_param_value) # ok

print(get_amzn_product_data(item_id, responseGroup))
# root = xmlDoc.parse(get_amzn_product_data(item_id, responseGroup)).getroot()
# data = xmlDoc.fromstring(get_amzn_product_data(item_id, responseGroup).read())
# print(data[1])
# print(root.tag)
# for datum in data.iter('*'):
# 	print(datum.tag)


# for element in root.iter('*'):
# 	print(element.tag)

