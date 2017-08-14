import json, os
import sys
# append path to keys for import
sys.path.append('C:\\Code\\trade_cat_scripts')
import keys
import urllib.request

metadata_token = os.environ['VLB_TOKEN_METADATA']

def get_isbn(isbn):

	url = 'http://api.vlb.de/api/v1/product/'+str(isbn)+'/isbn13'
	response = get_request(url)
	data = json.loads(response.read())
	return data

def add_headers(request):
	
	request.add_header('Authorization', 'Bearer '+metadata_token)
	request.add_header('Content-Type', 'application/json')
	request.add_header('Accept', 'application/json')
	return request

def get_request(url):

    request = add_headers(urllib.request.Request(url))
    try:
    	return urllib.request.urlopen(request)
    except urllib.request.HTTPError as err:
    	print(err)
	

print(get_isbn(9783476043306)['id'])
# get_request('http://api.vlb.de/api/v1/product/9783476043306/isbn13')


