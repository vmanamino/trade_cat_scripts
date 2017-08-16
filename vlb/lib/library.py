import json, os
import sys
# append path to keys for import
sys.path.append('C:\\Code\\trade_cat_scripts')
import keys
import urllib.request

metadata_token = os.environ['VLB_TOKEN_METADATA']

def get_isbn(isbn):

	url = 'http://api.vlb.de/api/v1/product/'+str(isbn)+'/isbn13'
	return response_dict(get_request(url))	

def add_headers(request):
	
	request.add_header('Authorization', 'Bearer ')#+metadata_token)
	request.add_header('Content-Type', 'application/json')
	request.add_header('Accept', 'application/json')
	return request

def get_request(url):

    request = add_headers(urllib.request.Request(url))
    try:
    	return urllib.request.urlopen(request)
    except urllib.request.HTTPError as err:
    	return err    	
	
def response_dict(response):
	data_dict = {}
	data = json.loads(response.read())
	data_dict['content'] = data

	if response.code == 200:
		data_dict['code'] = response.code		
	else:
		data_dict['code'] = response.code		

	return data_dict


print(get_isbn(9783476043306))
# # get_request('http://api.vlb.de/api/v1/product/9783476043306/isbn13')


