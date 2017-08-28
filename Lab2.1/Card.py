import json
import requests
import pprint



r = requests.get('https://lookup.binlist.net/52788300')
pprint.pprint(r.json())




