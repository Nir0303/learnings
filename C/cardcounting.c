#include <stdio.h>
int main() {
	char card[3];
	scanf("%2s",card);
	int value;
	if ((card[0]=='3') || (card[0]=='4') ||(card[0]=='5') || (card[0]=='6')){
		value= atoi(card)+1;
	}else if ((card[0]=='1') || (card[0]=='K') ||(card[0]=='Q') || (card[0]=='J')){
		value=10;
	}else{
		return 1;
	}
	printf("Card value %d\n",value);
	if (value >=4 && value<=7){
		printf("Value has gone up");
	} else {
		printf("Value has gone down");
	}
	return 0;
}