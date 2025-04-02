#include <stdio.h>

int main(){
	int num1;
	int num2;
	int num3;
	int result;

	printf("input 1:\n");
	scanf("%d", &num1);
	printf("input 2:\n");
	scanf("%d", &num2);
	printf("input 3:\n");
	scanf("%d", &num3);

	if(num2 > num3){
		if (num1 > num2){
			result = num1+num2/num3;
		}else{
			result = num1*num2+num3;
		}
	}else{
		if (num2 > num1){
			result = num1-num2-num3;
		}else{
			result = num1*num2*num3;
		}
	}

	printf("result %d\n", result);
}
