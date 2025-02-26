#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void not_vulnerable_function(){
	char input[32];
	printf("enter your input: ");
	fgets(input, sizeof(input), stdin);
	printf("you entered: %s\n", input);
}

int main(){
	not_vulnerable_function();
	printf("exit\n");
	return 0;
}


