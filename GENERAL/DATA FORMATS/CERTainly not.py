from Crypto.PublicKey import RSA

with open("C:\\Users\\Admin\\Downloads\\ex\\2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der", "rb") as f:
    cert = f.read()

print(RSA.importKey(cert).n)