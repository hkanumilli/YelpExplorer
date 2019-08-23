import requests
from pprint import pprint
from urllib.parse import quote

### Yelp API Credentials - Insert Your Own Below ###
API_KEY = ''

### API Constants ###
API_HOST = "https://api.yelp.com"
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.
SEARCH_LIMIT = 50

### Connect to Database and POST requests ###
def request(host, path, token = API_KEY, url_params = None):
	url = '{0}{1}'.format(host, quote(path.encode('utf8')))
	headers = { 'Authorization': 'Bearer %s' % token}
	print('Querying {0}....'.format(url))
	return (requests.request('GET', url, headers = headers, params = url_params)).json()

### Initialize Search Paramters ###
def search_params(term, location, price):
	parameters = {}
	parameters['term'] = term
	parameters['location'] = location
	parameters['price'] = price
	parameters['limit'] = SEARCH_LIMIT
	parameters['raidus'] = 40000
	return parameters

### Search Yelp Database ###
def search(token, parameters):
	parameters['term'] = parameters['term'].replace(' ', '+')
	parameters['location'] = parameters['location'].replace(' ', '+')
	return request(API_HOST, SEARCH_PATH, token, url_params = parameters)

### gets business id ###
def get_business(token, business_id): 
	return request(API_HOST, BUSINESS_PATH + business_id, token)



### main function ###
def query_api(term, location, price):
	parameters = search_params(term, location, price)
	searchResponse = search(API_KEY, parameters)
	restaurants = searchResponse.get('businesses')

	if not restaurants:
		print('No businesses found for {0} in {1}'.format(term, location))
		return None

	print('{0} businesses found for {1} in {2}'.format(len(restaurants), term, location))
	return restaurants


# uncomment and run to get list of restaurants and test out the main function
# pprint(query_api('coffee', 'seattle', 3))


