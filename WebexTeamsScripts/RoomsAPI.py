# Rooms API

# URL = "https://webexapis.com/v1/rooms" 	# "GET" -> List all roomms | "POST" -> create new room

# URL = "https://webexapis.com/v1/rooms/{roomId}"	# "Get" -> room details | "PUT" -> update room details | DELETE

# URL = "https://webexapis.com/v1/rooms/{roomId}/meetingInfo"	# "Get" -> room meeting details

# create new room:

import json
import requests
import pprint

URL = input('Enter API URL: ')

PAYLOAD = {"name": "Room name here"}

HEADERS = { "Authorization": "Bearer AOSNDSW878FV78FB8", "Content-Type": "application/json"}

RESPONSE = requests.request("POST", URL, headers=HEADERS, data=json.dumps(PAYLOAD))

pprint.pprint(json.loads(RESPONSE.text))
