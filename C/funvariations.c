#include <stdio.h>
int changevalue(int x,int y)
{
	x=x+1;
	y+=2;
}
void changevaluewithaddress(int *x,int *y)
{
	*x=*x+1;
	*y+=2;
}
int main() {
	int a=5;
	int b=6;
	changevalue(a,b);
	printf("%d,%d\n",a,b);
	changevaluewithaddress(&a,&b);
	printf("%d,%d",a,b);
	return 0;
}