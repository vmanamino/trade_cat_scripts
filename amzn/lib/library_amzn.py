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
from urllib.parse import urlencode, quote_plus


amzn_id = os.environ['AMZN_DE_ACCESS_ID']
amzn_key = os.environ['AMZN_DE_ACCESS_KEY']
assoc_tag = os.environ['AMZN_ASSOC_TAG']


item_id = '9783476043306'

# create timestamp
date_time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')

date_time = urllib.parse.quote(date_time, safe='')
print(date_time)


# string to sign
s = ('http://webservices.amazon.de/onca/xml?AWSAccessKeyId='+amzn_id+'&AssociateTag='+assoc_tag+'&ContentType'
'=&IdType=ISBN&ItemId='+item_id+'&Operation=ItemLookup&ResponseGroup=OfferSummary&SearchIndex=Books&Service=AWSECommerceService&'
'Timestamp='+date_time)

# break string into pairs of param and value
pairs = s.split('?')
del pairs[0]
pairs = pairs[0].split('&')

# sort the pairs based on binary values
pairs.sort()


# join pairs again into a string
s = "&".join(pairs)

# begin building the request
verb = 'GET\n'
domain = 'webservices.amazon.de\n'
expression = '/onca/xml\n'
to_be_prepended = verb + domain + expression
s_to_send = to_be_prepended + s

# 
s_to_send = bytes(s_to_send, 'utf-8')
amzn_key = bytes(amzn_key, 'utf-8')
digest = hmac.new(amzn_key, msg=s_to_send, digestmod=hashlib.sha256).digest()

autograph = base64.b64encode(digest)
autograph = autograph.decode('utf-8')

signature = urllib.parse.quote(autograph, safe='')

signature_param_value = '&Signature='+signature

s_to_send_to_string = s_to_send.decode('utf-8')
s_as_stanza = s_to_send_to_string +''+signature_param_value
s_verb_removed = s_as_stanza[4:]
request = s_verb_removed.replace('\n', '').replace('xml', 'xml?')
http_prefix = 'http://'
url_request = http_prefix + request
print(url_request)


