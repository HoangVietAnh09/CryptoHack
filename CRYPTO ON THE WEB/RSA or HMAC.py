import jwt
import requests
import base64
from Crypto.Util.number import bytes_to_long



PUBLIC_KEY = 'MIIBCgKCAQEAvoOtsfF5Gtkr2Swy0xzuUp5J3w8bJY5oF7TgDrkAhg1sFUEaCMlR\nYltE8jobFTyPo5cciBHD7huZVHLtRqdhkmPD4FSlKaaX2DfzqyiZaPhZZT62w7Hi\ngJlwG7M0xTUljQ6WBiIFW9By3amqYxyR2rOq8Y68ewN000VSFXy7FZjQ/CDA3wSl\nQ4KI40YEHBNeCl6QWXWxBb8AvHo4lkJ5zZyNje+uxq8St1WlZ8/5v55eavshcfD1\n0NSHaYIIilh9yic/xK4t20qvyZKe6Gpdw6vTyefw4+Hhp1gROwOrIa0X0alVepg9\nJddv6V/d/qjDRzpJIop9DSB8qcF1X23pkQIDAQAB'
url = 'https://web.cryptohack.org/rsa-or-hmac/authorise'

# encdoe = jwt.encode({"username": "admin", "admin": True}, PUBLIC_KEY, algorithms=['HS256', 'RS256'])
print(PUBLIC_KEY)