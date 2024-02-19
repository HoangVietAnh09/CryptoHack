import jwt
import requests
encoded = jwt.encode({'username':'admin', 'admin': True}, 'secret', algorithm='HS256')
url = 'http://web.cryptohack.org/jwt-secrets/authorise/' + encoded + '/'
flag =  requests.get(url)
print(flag.text)
