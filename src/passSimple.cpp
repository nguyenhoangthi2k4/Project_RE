#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
	char input[20];
	printf("Xin chao! Hay nhap mat khau: ");
	scanf("%s", input);
	if(strcmp(input, "sinhvienIT")==0)
		printf("Mat khau hop le!\n");
	else
		printf("Nhap sai mat khau!\n");
	system("pause");
	return 0;
}