import datetime
# import requests
# import time
import hmac
import hashlib
import base64
from hashlib import sha256
# import asyncio
# import aiohttp
# import async_timeout
import os
import sys
# append path to keys for import
sys.path.append('C:\\Code\\trade_cat_scripts')
import keys
import socket
import time
import urllib
import urllib.request
from urllib.parse import urlencode, quote_plus
from xml.etree.ElementTree import parse
from xml.dom import minidom

timeout = 10
socket.setdefaulttimeout(timeout)

ns = {'aws':'http://webservices.amazon.com/AWSECommerceService/2011-08-01'}
# from library_common import response_dict

# amazon xml namespace for parsing xml doc
# ns = {'aws':'http://webservices.amazon.com/AWSECommerceService/2011-08-01'}

# set these parameter for future development
# id_type = 'ISBN'
# item_id = '9783476043306'
# operation = 'ItemLookup'
# responseGroup = 'OfferSummary'
# searchIndex = 'Books'

# def collate_amzn_data(title_info, availability, price, cover):
# 	# dict, imitate json
# 	pass

def collate_amzn_data(item_id, response_group): # add other attributes of amzn prod.	
	response, msg = amzn_request(get_amzn_url(item_id, response_group))	
	return parse_amzn_response(response, item_id, msg, response_group)	
	
# under construction
def parse_amzn_response(response, item_id, msg, response_group):
	# need to set keys conditionally on response group
	amzn_prod_dict = {}	
	if response_group == 'ItemAttributes':
		# everythin upt to if doc root find items, put in a separate function
		if response != 'no response':		
			if response.status == 200:			
				doc = parse(response)			
				doc_root = doc.getroot()							
					# find all children
				if doc_root.find('aws:Items', ns):									
					children = doc_root.find('aws:Items', ns)
					print(children)
					# print(children)
					title, isbn = get_item_attrs(children, item_id)
					amzn_prod_dict['isbn'] = isbn
					amzn_prod_dict['title_info'] = title								
				else:
					amzn_prod_dict['isbn'] = 'No children of Items'
					amzn_prod_dict['title_info'] = 'No children of Items'	
			else:
				amzn_prod_dict['isbn'] = response.status
				amzn_prod_dict['title_info'] = response.status
		else:
			amzn_prod_dict['isbn'] = msg
			amzn_prod_dict['title_info'] = msg

	if response_group == 'OfferFull':
		if response != 'no response':
			if response.status == 200:
				doc = parse(response)
				doc_root = doc.getroot()
				if doc_root.find('aws:Items', ns):
					children = doc_root.find('aws:Items', ns)
					print(children)
					merchant, price, saved, availability = get_offer_listing(children, item_id)
					amzn_prod_dict['merchant'] = merchant
					amzn_prod_dict['price'] = price
					amzn_prod_dict['amount_saved'] = saved
					amzn_prod_dict['availability'] = availability
				else:
					amzn_prod_dict['merchant'] = 'no children of Items'
					amzn_prod_dict['price'] = 'no children of Items'
					amzn_prod_dict['amount_saved'] = 'no children of Items'
					amzn_prod_dict['availability'] = 'no children of Items'
			else:
				amzn_prod_dict['merchant'] = response.status
				amzn_prod_dict['price'] = response.status
				amzn_prod_dict['amount_saved'] = response.status
				amzn_prod_dict['availability'] = response.status

		else:
			amzn_prod_dict['merchant'] = msg
			amzn_prod_dict['price']	= msg
			amzn_prod_dict['amount_saved'] = msg
			amzn_prod_dict['availability'] = msg	

	# 	if response != 'no response':

		# if response != 'no response':
		# 	if response.status == 200:
		# 		doc = parse(response)			
		# 		doc_root = doc.getroot()
		# 		if doc_root.find('aws:Items', ns):
		# 			for child in doc_root.findall('aws:Items', ns):
		# 				if child.find('aws:Item', ns):														
		# 					for progeny in child.findall('aws:Item', ns):
		# 						if progeny.find('aws:Offers', ns):
		# 							for kid in progeny.findall('aws:Offers', ns):
		# 								if kid.find('aws:Offer', ns):
		# 									for grandkid in kid.findall('aws:Offer', ns):
		# 										if grandkid.find('aws:OfferListing', ns):
		# 											for proprogeny in grandkid.findall('aws:OfferListing', ns):
		# 												if proprogeny.find('aws:Price', ns):
		# 													for kind in proprogeny.findall('aws:Price', ns):
		# 														if kind.find('aws:FormattedPrice', ns) is not None:
		# 															price = kind.find('aws:FormattedPrice', ns)
		# 															amzn_prod_dict['price'] = price
		# 														else:
		# 															amzn_prod_dict['price'] = 'no FormattedPrice element'	
		# 												else:
		# 													amzn_prod_dict['price'] = 'no Price element'
		# 												if proprogeny.find('aws:AvailabilityAttributes', ns):
		# 													for nino in proprogeny.findall('aws:AvailabilityAttributes', ns):
		# 														if nino.find('aws:AvailabilityType', ns) is not None:
		# 															availability = nino.find('aws:AvailabilityType', ns)
		# 															amzn_prod_dict['availability'] = availability
		# 														else:
		# 															amzn_prod_dict['availability'] = 'no AvailabilityType element'
		# 												else:
		# 													amzn_prod_dict['availability'] = 'no AvailabilityAttributes element'																		
		# 										else:
		# 											amzn_prod_dict['price'] = 'no OfferListing element'
		# 											amzn_prod_dict['availability'] = 'no OfferListing element'
		# 								else:
		# 									amzn_prod_dict['price'] = 'no Offer element'
		# 									amzn_prod_dict['availability'] = 'no Offer element'
		# 						else:
		# 							amzn_prod_dict['price'] = 'no Offers element'
		# 							amzn_prod_dict['availability'] = 'no Offers element'
		# 				else:
		# 					amzn_prod_dict['price'] = 'no Items element'
		# 					amzn_prod_dict['availability'] = 'no Items element'
		# 		else:
		# 			amzn_prod_dict['price'] = 'no Items element'
		# 			amzn_prod_dict['availability'] = 'no Items element'
		# 	else:
		# 		amzn_prod_dict['price'] = response.status
		# 		amzn_prod_dict['availability'] = response.status
		# else:
		# 	amzn_prod_dict['price'] = msg
		# 	amzn_prod_dict['availability'] = msg
	return amzn_prod_dict

# def parse_amzn_responses(data, item_id): 	
# 	amzn_prod_dict = {'isbn': '', 'title_info':'', 'availability': '', 'price_info': '', 'cover_info': ''}
# 	response_count = 0
# 	# print(len(data))
# 	for datum in data:

# 		# response count tracks specific response, needed to assign error code to dict key
# 		response_count += 1
# 		# print(response_count)
# 		# print(amzn_prod_dict)
# 		# check status success, or failure, on failure fill dict with appropriate message
# 		# print(datum.status)		
# 		if datum.status is 200:
# 			print(datum.status)
# 			doc = parse(datum)
# 			doc_root = doc.getroot()
# 			for elem in doc_root.findall('aws:OperationRequest', ns):
# 				args = elem.find('aws:Arguments', ns)
# 				for arg in args.findall('aws:Argument', ns):
# 					# print(arg.tag)
# 					arg_name = arg.get('Name')
# 					# print(arg_name)
# 					if arg_name == 'ResponseGroup':					
# 						arg_val = arg.get('Value')					
# 						if arg_val == 'OfferSummary':
# 							if doc_root.find('aws:Items', ns): # too much repitiion
# 								for children in doc_root.findall('aws:Items', ns): # too much repitition
# 									if children.find('aws:Item', ns): # too much repitition
# 										child = children.find('aws:Item', ns) # too much repitition
# 										if 	child.find('aws:OfferSummary', ns):		
# 											progeny = child.find('aws:OfferSummary', ns)
# 											if progeny.find('aws:LowestNewPrice', ns):
# 												price_wrapper = progeny.find('aws:LowestNewPrice', ns)
# 												if price_wrapper.find('aws:FormattedPrice', ns) is not None:
# 													price_info = price_wrapper.find('aws:FormattedPrice', ns)																						
# 													amzn_prod_dict['price_info'] = price_info.text[4:]
# 												else:
# 													amzn_prod_dict['price_info'] = 'None'
# 											else:
# 												amzn_prod_dict['price_info'] = 'None'
# 										else:
# 											amzn_prod_dict['price_info'] = 'None'
# 									else:
# 										amzn_prod_dict['price_info'] = 'None'
# 							else:
# 								amzn_prod_dict['price_info'] = 'None'							
# 						if arg_val == 'OfferListings':							
# 							if doc_root.find('aws:Items', ns): # too much repitiion
# 								for children in doc_root.findall('aws:Items', ns): # too much repitition
# 									if children.find('aws:Item', ns): # too much repitition
# 										child = children.find('aws:Item', ns) # too much repitition
# 										if child.find('aws:Offers', ns):
# 											progeny = child.find('aws:Offers', ns)
# 											if progeny.find('aws:Offer', ns):
# 												offer = progeny.find('aws:Offer', ns)
# 												if offer.find('aws:OfferListing', ns):
# 													offer_listing = offer.find('aws:OfferListing', ns)
# 													if offer_listing.find('aws:AvailabilityAttributes', ns):
# 														availability_attrs = offer_listing.find('aws:AvailabilityAttributes', ns)
# 														if availability_attrs.find('aws:AvailabilityType', ns) is not None:
# 															availability = availability_attrs.find('aws:AvailabilityType', ns)
# 															amzn_prod_dict['availability'] = availability.text
# 														else:
# 															amzn_prod_dict['availability'] = 'None'	
# 													else:
# 														amzn_prod_dict['availability'] = 'None'													
# 												else:
# 													amzn_prod_dict['availability'] = 'None'	
# 											else:
# 												amzn_prod_dict['availability'] = 'None'
# 										else:
# 											amzn_prod_dict['availability'] = 'None'
# 									else:
# 										amzn_prod_dict['availability'] = 'None'
# 							else:
# 								amzn_prod_dict['availability'] = 'None'								

# 						if arg_val == 'Images':
# 							if doc_root.find('aws:Items', ns): # too much repitition
# 								for children in doc_root.findall('aws:Items', ns): # too much repitition
# 									if children.find('aws:Item', ns): # too much repitition
# 										child = children.find('aws:Item', ns) # too much repitition
# 										if child.find('aws:MediumImage', ns):
# 											progeny = child.find('aws:MediumImage', ns)
# 											if progeny.find('aws:URL', ns) is not None:
# 												url = progeny.find('aws:URL', ns)
# 												amzn_prod_dict['cover_info'] = url.text
# 											else:
# 												amzn_prod_dict['cover_info'] = 'None'
# 										else:
# 											amzn_prod_dict['cover_info'] = 'No cover'
# 							else:
# 								amzn_prod_dict['cover_info'] = 'No cover'
							
# 						if arg_val == 'ItemAttributes':	
# 							if doc_root.find('aws:Items', ns):
# 								for children in doc_root.findall('aws:Items', ns):
# 									if children.find('aws:Item', ns):										
# 										grandchildren = children.findall('aws:Item', ns)
# 										print('# of grandchildren', end=': ')
# 										print(len(grandchildren))								
# 										title, isbn = get_item_attrs(grandchildren, item_id)
# 										amzn_prod_dict['isbn'] = isbn
# 										amzn_prod_dict['title_info'] = title
# 									else:
# 										amzn_prod_dict['isbn'] = 'None'
# 										amzn_prod_dict['title_info'] = 'None'		
# 							else:
# 								amzn_prod_dict['isbn'] = 'None'
# 								amzn_prod_dict['title_info'] = 'None'										
# 		else:
# 			msg = None
# 			if datum.status:
# 				msg = datum.status
# 			if response_count is 1:
# 				amzn_prod_dict['price_info'] = msg
# 			if response_count is 2:
# 				amzn_prod_dict['availability'] = msg
# 			if response_count is 3:
# 				amzn_prod_dict['cover_info'] = msg
# 			if response_count is 4:
# 				amzn_prod_dict['isbn'] = msg
# 				amzn_prod_dict['title_info'] = msg
# 	print(amzn_prod_dict)
# 	return amzn_prod_dict
def get_item_attrs(elements, item_id):	
	isbn = ''
	title = ''
	# isbns_to_check = {'EISBN': '', 'EAN': ''}
	isbns_to_check = []
	if elements.findall('aws:Item', ns):
		items = elements.findall('aws:Item', ns)
		for item in items:
			if item.find('aws:ItemAttributes', ns):
				item_attrs = item.find('aws:ItemAttributes', ns)				
				if item_attrs.find('aws:EISBN', ns) is not None:
					eisbn = item_attrs.find('aws:EISBN', ns)
					isbns_to_check.append(eisbn.text)
				if item_attrs.find('aws:EAN', ns) is not None:
					ean = item_attrs.find('aws:EAN', ns)
					isbns_to_check.append(ean.text)
				if isbns_to_check: # superfluous, could use for else statement, but makes parsing clearer
					for each_isbn in isbns_to_check:
						print(each_isbn)
						if each_isbn == item_id:
							isbn = each_isbn
							if item_attrs.find('aws:Title', ns) is not None:
								title = item_attrs.find('aws:Title', ns)
								title = title.text	
							else:
								title = 'No Title element'
							# return title, isbn
					if not isbn:
						isbn = 'bflux ISBN did not match'
						if item_attrs.find('aws:Title', ns) is not None:
							title = item_attrs.find('aws:Title', ns)
							title = title.text	
						else:
							title = 'No Title element'
				else:
					isbn = 'No ISBNs to check'
					title = 'No ISBNs to check'
				# return title, isbn
			else:
				isbn = 'No ItemAttr elements'
				title = 'No ItemAttr elements'				
	else:
		isbn = 'No Item elements'
		title = 'No Item elements'
	return title, isbn

def get_offer_listing(elements, item_id):
	merchant = ''
	price = ''
	amount_saved = ''
	availability = ''
	if elements.findall('aws:Item', ns):
		items = elements.findall('aws:Item', ns)
		for item in items:
			if item.find('aws:Offers', ns):
				item_offers = item.find('aws:Offers', ns)
				if item_offers.findall('aws:Offer', ns):
					item_offer_children = item_offers.findall('aws:Offer', ns)
					for each_offer_child in item_offer_children:
						if each_offer_child.find('aws:Merchant', ns):
							merchant_element = each_offer_child.find('aws:Merchant', ns)
							if merchant_element.find('aws:Name', ns) is not None:
								merchant_name = merchant_element.find('aws:Name', ns)
								if merchant_name.text == 'Amazon.de': # too language specific, need to change
									merchant = merchant_name.text
									if each_offer_child.find('aws:OfferListing', ns):
										offer_listing = each_offer_child.find('aws:OfferListing', ns)
										if offer_listing.find('aws:Price', ns):
											price_element = offer_listing.find('aws:Price', ns)
											if price_element.find('aws:Amount', ns) is not None:
												price_amount_elem = price_element.find('aws:Amount', ns)
												price_int = int(price_amount_elem.text)/100
												price = '%.2f' % price_int
											else:
												price = 'No Amount element in Price'
										else:											
											price = 'No Price element'											
										if offer_listing.find('aws:AmountSaved', ns):
											amountSaved = offer_listing.find('aws:AmountSaved', ns)
											if amountSaved.find('aws:Amount', ns) is not None:
												amount_saved_elem = amountSaved.find('aws:Amount', ns)
												amount_saved_int = int(amount_saved_elem.text)/100
												amount_saved = '%.2f' % amount_saved_int
											else:
												amount_saved = 'No Amount in AmountSaved'
										else:
											amount_saved = 'No AmountSaved element'
										if offer_listing.find('aws:AvailabilityAttributes', ns):
											availability_attrs_element = offer_listing.find('aws:AvailabilityAttributes', ns)
											if availability_attrs_element.find('aws:AvailabilityType', ns) is not None:
												availability = availability_attrs_element.find('aws:AvailabilityType', ns)
												availability = availability.text
											else:
												availability = 'No AvailabilityType element'
										else:
											availability = 'No AvailabilityAttributes'
									else:
										# merchant = 'No OfferListing element'
										price = 'No OfferListing element'
										amount_saved = 'No OfferListing element'
										availability = 'No OfferListing element'			
							else:
								merchant = 'No Merchant Name element'
								price = 'No Merchant Name element'
								amount_saved = 'No Merchant Name element'
								availability = 'No Merchant Name element'	
						else:
							merchant = 'No Merchant element'
							price = 'No Merchant element'
							amount_saved = 'No Merchant element'
							availability = 'No Merchant element'							
					if merchant_name.text and merchant_name.text != 'Amazon.de':
						merchant = 'Amazon.de not listed as merchant in any Offer'
						price = 'No OfferListing element'
						amount_saved = 'No OfferListing element'
						availability = 'No OfferListing element'
				else:
					merchant = 'No Offer elements'
					price = 'No Offer elements'
					amount_saved = 'No Offer elements'
					availability = 'No Offer elements'	
			else:
				merchant = 'No Offers element'
				price = 'No Offers element'
				amount_saved = 'No Offers element'
				availability = 'No Offers element'		
	else:
		merchant = 'No Item elements'
		price = 'No Item elements'
		amount_saved = 'No Item elements'
		availability = 'No Item elements'

	return merchant, price, amount_saved, availability

def amzn_request(url):
    request = urllib.request.Request(url)
    response = 'no response'
    msg = ''
    tries = 10
    while tries > 0:
	    try:
	    	# add timeout
	    	response = urllib.request.urlopen(request, timeout=10)
	    except urllib.request.HTTPError as http_err:
	    	tries -= 1	    	
	    	response = http_err
	    	msg = 'http error'
	    	time.sleep(2)
	    except socket.timeout:
	    	tries -= 1	    	
	    	msg = 'socket timeout'
	    	time.sleep(2)
	    except socket.error:
	    	tries -= 1	    	
	    	msg = 'socket error'
	    	time.sleep(2)
	    else:
	    	return response, msg
    return response, msg
    

# response group param

# def get_amzn_response(item_id, responseGroup):
	
# 	response = amzn_request(get_amzn_url(item_id, responseGroup))
	
# 	return response

def gather_amzn_responses(item_id):		

	amzn_data = []

	amzn_data.append(amzn_request(get_amzn_url(item_id, 'OfferSummary')))	
	time.sleep(8)	
	amzn_data.append(amzn_request(get_amzn_url(item_id, 'Images')))	
	time.sleep(8)	
	amzn_data.append(amzn_request(get_amzn_url(item_id, 'OfferListings')))	
	time.sleep(8)	
	amzn_data.append(amzn_request(get_amzn_url(item_id, 'ItemAttributes')))

	return amzn_data

	# loop = asyncio.get_event_loop()
	# amzn_data = loop.run_until_complete(asyncio.gather(
	# 	amzn_request(get_amzn_url(item_id, 'OfferSummary')),
	# 	amzn_request(get_amzn_url(item_id, 'Images')),
	# 	amzn_request(get_amzn_url(item_id, 'OfferListings')),
	# 	amzn_request(get_amzn_url(item_id, 'ItemAttributes'))))
	# return amzn_data	
    
def get_amzn_url(isbn, responseGroup):

	s = create_string(isbn, responseGroup)
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
	id_type = 'ISBN'
	operation = 'ItemLookup'
	searchIndex = 'Books'

	# create timestamp
	date_time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')

	date_time = urllib.parse.quote(date_time, safe='')
	# print(date_time)
	
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

# print(get_amzn_url('9783319661391', "Images"))

# collate_amzn_data(item_id)
# print(get_amzn_url('9788847057661', 'Images'))

# this PRINT isbn has several items on amazon 9783662463727 and has EISBN for Kindle Versions 
# print(collate_amzn_data('9783662463727'))
# print(get_amzn_url('9783662463727', 'ItemAttributes'))

# this is an actual eisbn 9783662463734
# print(collate_amzn_data('9783662463734'))
# print(get_amzn_url('9783662463734', 'Images'))

# print isbn 9783662467862
# print(collate_amzn_data('9783662467862'))

# print isbn 9789462651227
# print(collate_amzn_data('9783662451151'))

# prices displayed not available in api response
# print(get_amzn_url('9783642312199', 'OfferSummary'))

# print(get_amzn_url('9783662469149', 'Large'))

# offersummary with no item
# print(get_amzn_url('9783642361722', 'OfferSummary'))

# 9783642361722 no offers
# print(get_amzn_url('9783642361722', 'OfferListings'))

# print(gather_amzn_responses('9789462651227'))

# print(get_amzn_url('9783662500330', 'OfferFull'))

# print(collate_amzn_data('9783642450525'))

# print(collate_amzn_data('9783642450525', 'ItemAttributes'))
# print(get_amzn_url('9783642450525', 'ItemAttributes'))

# print(get_amzn_url('9783642545962', 'OfferFull'))

# this isbn has different on sale type offer
# print(get_amzn_url('9783642361715', 'OfferFull'))

# print(get_amzn_url('9788847057661', 'OfferFull'))

# good example of confusing amazon grouping
# print(get_amzn_url('9789462651050', 'ItemAttributes'))

# print(get_amzn_url('9783662494844', 'ItemAttributes'))
# print(collate_amzn_data('9783642404061', 'ItemAttributes'))
# print(get_amzn_url('9783642404061', 'ItemAttributes'))

# print(get_amzn_url('9783662494844', 'OfferFull'))
print(collate_amzn_data('9788847057661', 'OfferFull'))