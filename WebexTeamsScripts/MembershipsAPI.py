# Membership API

# URL = "https://webexapis.com/v1/membership" 	# "GET" -> List memberships | "POST" -> add new member

# URL = "https://webexapis.com/v1/memberships/{membershipId}"	# "Get" -> member details | "PUT" -> update member details | DELETE


# add new member:

import json
import requests
import pprint

URL = input('Enter API URL: ')

PAYLOAD = {"roomId": "Room ID here", "personEmail": "newUser@email", "personDisplayName": "Display name here", "isModerator": "false"}

HEADERS = { "Authorization": "Bearer AOSNDSW878FV78FB8", "Content-Type": "application/json"}

RESPONSE = requests.request("POST", URL, headers=HEADERS, data=json.dumps(PAYLOAD))

pprint.pprint(json.loads(RESPONSE.text))
