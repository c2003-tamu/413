#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void vulnerable_function(){
	char input[32];
	printf("enter your input: ");
	gets(input);
    	printf("Address of buffer: %p\n", (void*)input);
	printf("you entered: %s\n", input);
}

int main(){
	vulnerable_function();
	printf("exit\n");
	return 0;
}


