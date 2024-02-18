def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

p = 26513
q = 32321
# p*u + q*v = gcd(p,q)
v = pow(q, -1, p)
v -= p
u = (gcd(p, q) - (q*v))//p
print(max(u, v))
