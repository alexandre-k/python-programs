import json
import requests
movie_json = '''
{
"Title": "Circuit",
"Year": "2001",
"Runtime": "130 min",
"Country": "USA"
}
'''

movie_data = json.loads(movie_json)
print(movie_data)
url = 'http://www.omdbapi.com/?y=&plot=short&r=json&s=silicon'

resp = requests.get(url)
search_results = resp.json()['Search']
print(search_results)
for m in search_results:
    print(' * ' + m['Title'])

print(json.dumps(movie_data))
