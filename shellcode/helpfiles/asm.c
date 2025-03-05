#include <stdio.h>
int add_three() {
    int result;
    __asm__(
        "xor %%eax, %%eax;"
        "inc %%eax;"
        "xor %%ebx, %%ebx;"
        "inc %%ebx;"
        "xor %%ecx, %%ecx;"
        "inc %%ecx;"
        "addl %%ebx, %%eax;"
        "addl %%ecx, %%eax;"
        "movl %%eax, %0"
        : "=r" (result)
        :
        : "%eax", "%ebx", "%ecx"
    );
    
    return result;
}

int main(){
    int result = add_three();
    printf("result of adding 1 and 1 and 1 is: %d\n", result);
    return 0;
}

