#include <stdio.h>

int add_three() {
    int firstval = 1;
    int secondval = 1;
    int thirdval = 1;

    int result = firstval + secondval + thirdval;
    return result;
}

int main(){
    int result = add_three();
    printf("result of adding 1 and 1 and 1 is: %d\n", result);
    return 0;
}

