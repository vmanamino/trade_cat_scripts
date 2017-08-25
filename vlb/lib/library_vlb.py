from openpyxl import load_workbook
import string
import json, os
import sys
# append path to keys for import
sys.path.append('C:\\Code\\trade_cat_scripts')
import keys
import urllib.request
# import pickle

metadata_token = os.environ['VLB_TOKEN_METADATA']

def get_product_data(isbn):

	url = 'http://api.vlb.de/api/v1/product/'+str(isbn)+'/isbn13'
	return response_dict(get_request(url))	

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
    	return err    	
	
def response_dict(response):
	data_dict = {}
	data = json.loads(response.read())

	# want to create test data	
	# with open('vlb_json_test.json', 'w') as json_dump:
	# 	json_dump.write(str(data))

	data_dict['content'] = data

	if response.code == 200:
		data_dict['code'] = response.code		
	else:
		data_dict['code'] = response.code		

	# # test data	
	# with open('C:\\Code\\trade_cat_scripts\\tests\\dataset\\vlb_test_pickle_error.txt', 'wb') as test_pickle:
	# 	pickle.dump(data_dict, test_pickle)

	return data_dict

def get_frontcover(mediafiles):
	# get the first 04 (front cover) OR 06 (front cover High Quality)
	flag = False
	for file in mediafiles:
		if file['type'] == '06':
			flag = True
			return file['link']
		elif file['type'] == '04':
			flag = True
			return file['link']	
	if not flag:
			return "No front cover"

# add AT and CH
def dach_prices(prices):
	flag_de = False
	flag_at = False
	flag_ch = False
	dachs = {'DE':'', 'AT':'', 'CH':''}
	for price in prices:
		if price['country'] == 'DE':
			flag_de = True
			dachs['DE'] = price['value']
		if price['country'] == 'AT':
			flag_at = True
			dachs['AT'] = price['value']
		if price['country'] == 'CH':
			flag_ch = True
			dachs['CH'] = price['value']

	if not flag_de:
		dachs['DE'] = "No German Price"
	if not flag_at:
		dachs['AT'] = "No Austrian Price"
	if not flag_ch:
		dachs['CH'] = "No Swiss Price"

	return dachs



'''
function to get the data from Delilah excel file
'''
def get_sheetdata(file):

	wb = load_workbook(file)
	names = wb.get_sheet_names()
	return wb[names[0]] # data returned

def get_attributes(data):
	pass
	
# print(get_product_data(9783476043306))
# print(get_product(9781430261063))
# print(get_product(9781484213933))
# print(get_product_data(9783658147747))
# # get_request('http://api.vlb.de/api/v1/product/9783476043306/isbn13')


