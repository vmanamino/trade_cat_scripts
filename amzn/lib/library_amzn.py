import datetime
import requests
# import time
import hmac
import hashlib
import base64
from hashlib import sha256
import asyncio
import aiohttp
import async_timeout
import os
import sys
# append path to keys for import
sys.path.append('C:\\Code\\trade_cat_scripts')
import keys
import urllib
# import urllib.request
from urllib.parse import urlencode, quote_plus
from xml.etree.ElementTree import parse
from xml.dom import minidom

sys.path.append('C:\\Code\\trade_cat_scripts\\lib')
# from library_common import response_dict


# set these parameter for future development
id_type = 'ISBN'
item_id = '9783476043306'
operation = 'ItemLookup'
responseGroup = 'OfferSummary'
searchIndex = 'Books'


# called only on status success
def get_amzn_product_data(value, responseGroup_items):
	if value == 'OfferSummary':
		print('get amazon price data')
		
	if value == 'OfferListings':
		print('get amazon availability data')		
		
	if value == 'ItemAttributes':
		print('get amazon title data')
		for parent in responseGroup_items:
			print('item attrs')
			print(parent.tag)

		
	if value == 'Images':
		print('get amazon image data')

async def amzn_request(url):

    request = urllib.request.Request(url)
    try:
    	# add timeout
    	return urllib.request.urlopen(request)
    except urllib.request.HTTPError as err:
    	return err

def gather_amzn_responses(item_id):		

	loop = asyncio.get_event_loop()
	amzn_data = loop.run_until_complete(asyncio.gather(
		amzn_request(get_amzn_url(item_id, 'OfferSummary')),
		amzn_request(get_amzn_url(item_id, 'Images')),
		amzn_request(get_amzn_url(item_id, 'OfferListings')),
		amzn_request(get_amzn_url(item_id, 'ItemAttributes'))))
	return amzn_data	
    
def get_amzn_url(isbn, data_point):

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

# print(get_amzn_product_data(item_id, responseGroup))
# root = xmlDoc.parse(get_amzn_product_data(item_id, responseGroup)).getroot()
# data = xmlDoc.fromstring(get_amzn_product_data(item_id, responseGroup).read())
# print(data[1])
# print(root.tag)
# for datum in data.iter('*'):
# 	print(datum.tag)


# for element in root.iter('*'):
# 	print(element.tag)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.gather(main(item_id)))

# print(get_amzn_product_data(item_id, 'OfferListings'))

# get amazon product report data

print(get_amzn_url(item_id, "ItemAttributes"))

data = gather_amzn_responses(item_id)

avail_flag = None
title_flag = None
price_flag = None
image_flag = None

api_case_price = 1
api_case_images = 2
api_case_avail = 3
api_case_title = 4

api_case_count = 0

ns = {'aws':'http://webservices.amazon.com/AWSECommerceService/2011-08-01'}
for datum in data:
	print(datum.status)
	doc = parse(datum)
	doc_root = doc.getroot()
	for elem in doc_root.findall('aws:Items', ns):
		print(elem.tag)


# # def parse_amzn_responses
# for datum in data:
# 	# api_case_count += 1
# 	# if api_case_count is 1:
# 	# 	pass
# 	# if api_case_count is 2:
# 	# 	pass
# 	# if api_case_count is 3:
# 	# 	pass
# 	# if api_case_count is 4:
# 	# 	pass

# 	# make conditional on status, error or success
# 	print(datum.status)
# 	count = 0
# 	doc = parse(datum)
# 	doc_root = doc.getroot()
# 	print(doc_root.tag)
# 	for index, parent in enumerate(doc_root):
# 		print('parent', end=': ')
# 		print(parent.tag)
# 		for child in parent:
# 			count += 1
# 			if count is 3: # Arguments, below iterate through each argument
# 				for grandchild in child:					
# 					name = grandchild.attrib['Name']
# 					if name == 'ResponseGroup':
# 						value = grandchild.attrib['Value']
# 						print(name)
# 						print(value)
# 						if value == 'OfferSummary':
# 							print('Prices')
# 							price_flag = True
# 							print('Price/OfferSummary next tag', end=': ')
# 							responseGroup_items = doc_root[index +1]
# 							print(responseGroup_items)
# 							get_amzn_product_data(value, responseGroup_items)
# 						if value == 'OfferListings':
# 							print('Availability')
# 							avail_flag = True
# 							print('Availability/OfferListings next tag', end=': ')
# 							responseGroup_items = doc_root[index +1]
# 							print(responseGroup_items)
# 							get_amzn_product_data(value, responseGroup_items)
# 						if value == 'ItemAttributes':
# 							print('Title info')
# 							title_flag = True
# 							print('Title info/ItemAttributes next tag', end=': ')
# 							responseGroup_items = doc_root[index +1]
# 							print(responseGroup_items)
# 							get_amzn_product_data(value, responseGroup_items)
# 						if value == 'Images':
# 							print('Covers')
# 							image_flag = True
# 							print('Covers/Images next tag', end=': ')
# 							responseGroup_items = doc_root[index +1]
# 							print(responseGroup_items)
# 							get_amzn_product_data(value, responseGroup_items)


# called only on status success
def get_amzn_product_data(value, responseGroup_items):
	if value == 'OfferSummary':
		print('get amazon price data')
		
	if value == 'OfferListings':
		print('get amazon availability data')
		
	if value == 'ItemAttributes':
		print('get amazon title data')
		
	if value == 'Images':
		print('get amazon image data')
		



# def get_data()
	# for elements in doc.iterfind('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}ItemLookupResponse'):
		
# print(get_amzn_url(item_id, 'OfferSummary'))
	