#Author : Kim Kiogora  <kimkiogora@gmail.com>
#Usage  : BitPesa
#Date   : 2018-08-30, 12:07PM

import uuid
import requests
import json
import hashlib
import hmac

# Authentication details
API_KEY = 'YOUR_API_KEY' # From the developer portal
API_SECRET = 'YOUR_API_SECRET' # From the developer portal

# The request method and endpoint
API_URL = 'https:#api-sandbox.bitpesa.co/v1/senders'
API_METHOD = 'POST'

# Request-specific data
nonce = uuid.uuid4()# Must be unique per request
body = json.dumps({'sender': {
	    'country': 'UG',
	    'phone_country': 'UG',
	    'phone_number': '752403639',
	    'email': 'email@domain.com',
	    'first_name': 'Example',
	    'last_name': 'User',
	    'city': 'Kampala',
	    'street': 'Somewhere 17-3',
	    'postal_code': '798983',
	    'birth_date': '1970-01-01',
	    'documents': [{
	        'upload':'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAACXBIWXMAAAsT\nAAALEwEAmpwYAAAAB3RJTUUH4gEeCTEzbKJEHgAAAB1pVFh0Q29tbWVudAAA\nAAAAQ3JlYXRlZCB3aXRoIEdJTVBkLmUHAAAADElEQVQI12P4z8AAAAMBAQAY\n3Y2wAAAAAElFTkSuQmCC',
	        'upload_file_name': 'passport.png',
	        'metadata': { 'meta': 'data' }
	      }
	    ],
	    'ip': '127.0.0.1',
	    'metadata': { 'meta': 'data' }
  }})

hash = hashlib.sha512()
hash.update(body)
body_hash = hash.hexdigest()

to_sign = [
	str(nonce),
	API_METHOD,
	API_URL,
	body_hash
]

to_sign = '&'.join(to_sign)

auth_signature =  hmac.new(API_SECRET, to_sign, hashlib.sha512).hexdigest()

print 'DIGEST %r' % auth_signature

myheaders = [
  'Accept: application/json',
  'Content-Type: application/json',
  'Authorization-Key: ' + API_KEY,
  'Authorization-Nonce: ' + str(nonce),
  'Authorization-Signature: ' + str(auth_signature)
]

print 'Send request %s to URL %s headers %r' % (body,API_URL, myheaders)

try:
	print 'Send request %s to URL %s' % (body,API_URL)
	post_response = requests.post(url=API_URL, data=body, headers = myheaders)
	print "Response is %s" % post_response
except:
	_error = str(sys.exc_info()[1])
	print _error

