#include <stdio.h>
#include <string.h>

unsigned char shellcode[] = 
"\x31\xc0\x40\x31\xdb\x43\x31\xc9\x41\x01\xd8\x01\xc8\xc3";

int main() {
    ((void(*)( ))shellcode)( );
}
