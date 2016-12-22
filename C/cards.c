#include<stdio.h>
int main()
{
	char cards[3];
	scanf("%2s",&cards);
	if (cards[0]=='a'){
		printf("10\n");
	} else if (cards[0]=='b') {
		printf("20\n");
	}else {
		printf("Other\n");
		return 1;
	}
	printf("%s",cards);
	return 0;
}