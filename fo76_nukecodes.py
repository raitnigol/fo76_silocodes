# import requests and json to pull info from nukacrpyt json file
import requests
import json
# get the request from nukacrypt and load the content
j = json.loads(requests.get('https://nukacrypt.com/codes.json').content)

# print the outcome 
print("Site Alpha nuke code: " + j['alpha'])
print("Site Bravo nuke code: " + j['bravo'])
print("Site Charlie nuke code: " + j['charlie'])
