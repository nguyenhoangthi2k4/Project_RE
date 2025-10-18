#include <stdio.h>
#include <string.h>
#include <stdlib.h>
// XOR
void decrypt(char *buf, int len, char key) {
    for (int i = 0; i < len; i++) {
        buf[i] ^= key;
    }
}

int main() {
    char input[20];
    
    unsigned char encPass[] = { 0x26, 0x3C, 0x3B, 0x3D, 0x23, 0x3C, 0x30, 0x3B, 0x1C, 0x01, 0x00 };
    int len = 10; // độ dài password
    char key = 0x55;
    
	decrypt((char*)encPass, len, key); // sinhvienIT
	
    printf("Xin chao! Hay nhap mat khau: ");
	scanf("%s", input);
	
	
	if(strcmp(input, (char*)encPass)==0)
		printf("Mat khau hop le!\n");
	else
		printf("Nhap sai mat khau!\n");
	system("pause");

    return 0;
}
