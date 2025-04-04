#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	if(argc != 3){
		printf("Usage: %s <num1> <num2>\n", argv[0]);
		return 1;
	}
	int num1, num2;
	num1 = atoi(argv[1]);
	num2 = atoi(argv[2]);
	printf("%d\n", num1);
	printf("%d\n", num2);
	if (((num1 * num1) / num2) == 1) {
		printf("Granted\n");
	} else {
		printf("Denied\n");
	}

	return 0;
}
