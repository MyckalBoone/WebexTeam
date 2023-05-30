# Teams API


# API URL = "https://webexapis.com/v1/teams" 	# GET -> List all teams | POST -> Create new team

# API URL = "https://webexapis.com/v1/teams/{teamId}"	# GET -> details about team | PUT -> update details for team | DELETE

# Create new team below:

import json
import requests

URL = input('Enter API URL: ')

PAYLOAD = {"name": "Team name here"}

HEADERS = { "Authorization": "Bearer AOSNDSW878FV78FB8", "Content-Type": "application/json"}

RESPONSE = requests.request("POST", URL, headers=HEADERS, data=json.dumps(PAYLOAD)

print (RESPONSE)
