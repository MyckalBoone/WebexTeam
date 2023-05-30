# Messages API

# URL = "https://webexapis.com/v1/messages" 	# "GET" -> List messages | "POST" -> post a new message

# URL = "https://webexapis.com/v1/messages/{messageId}"	# "Get" -> message details | DELETE

# URL = "https://webexapis.com/v1/messages/direct"	# "Get" -> List one-to-one message

# Send message:

import json
import requests
import pprint

URL = input('Enter API URL: ')

PAYLOAD = {"roomId": "Room ID here", "text": "Enter message here"}

HEADERS = { "Authorization": "Bearer AOSNDSW878FV78FB8", "Content-Type": "application/json"}

RESPONSE = requests.request("POST", URL, headers=HEADERS, data=json.dumps(PAYLOAD))

pprint.pprint(json.loads(RESPONSE.text))
