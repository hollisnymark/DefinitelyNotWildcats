import json
import requests

config = {}
with open('config.json', 'r') as f:
    config = json.load(f)

auth_url = 'https://api.yelp.com/oauth2/token'

resp = requests.post(auth_url, data={'client_id': config['client_id'], 
                                    'client_secret': config['client_secret']})

token = resp.json()['access_token']

closed_count = 0
done = False
for x in range(0,20):
    if not done:
        offset = x*50
        search_url = 'https://api.yelp.com/v3/businesses/search?term=closed&location=10038&limit=50&offset={}&radius=1000'.format(offset)
        print(search_url)
        resp = requests.get(search_url, headers={'Authorization': 'bearer %s' % token})
        businesses = resp.json()['businesses']
        if len(businesses) == 0:
            done = True
        for biz in businesses:
            is_closed = biz['is_closed']
            is_closed = biz['is_closed']
            print(is_closed)
            if is_closed == 'false':
                closed_count += 1

print(closed_count)

