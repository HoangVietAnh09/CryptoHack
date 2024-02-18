from pwn import xor

input_str = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

for i in range(32):
    flag = xor(i, input_str).decode()
    if flag[:6] == 'crypto':
        print(flag)
