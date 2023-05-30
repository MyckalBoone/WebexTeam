import base64
import time
import math
import jwt


EXPIRATION = math.floor(time.time()) + 3600 # 1 hour in seconds from now

PAYLOAD = {"sub": "dev-ASC", "name": "devASC-guest", "iss": "GUEST_ISSUER_ID", "exp": EXPIRATION}

SECRET = base64.base64decode('GUEST_ISSUE_SECRET')

TOKEN = jwt.encode(PAYLOAD, SECRET)

print(TOKEN.decode('utf-8'))

HEADERS = {'Authorization': 'Bearer ' + TOKEN.decode('utf-8')}
