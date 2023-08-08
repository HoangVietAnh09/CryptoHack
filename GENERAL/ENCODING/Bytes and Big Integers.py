from Crypto.Util.number import long_to_bytes

key = 198614235373674103788888306985643587194108045477674049828655868730909536893

key = long_to_bytes(key)

print(key.decode())