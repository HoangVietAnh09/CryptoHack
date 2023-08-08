#!/usr/bin/env python3

from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373
q = 752708788837165590355094155871
p = 986369682585281993933185289261

phi = (q-1)*(p-1)
d = pow(e, -1, phi)

flag = pow(ct, d, n)
print(long_to_bytes(flag).decode())