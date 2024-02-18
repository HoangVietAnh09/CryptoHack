from Crypto.PublicKey import RSA

flag = open('c:\\Users\\Admin\\Downloads\\privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem', 'r')
flag = RSA.importKey(flag.read())
print(flag.d)