#include <stdio.h>
void msg (char *msg)
{
	printf("Niranjan says %s \n",msg);
	printf("Size of msg is %i \n",sizeof(msg));
}
int main () {
	char name[]="Hello world is too big";
	msg(name);
	printf("Size of name is %d\n",sizeof(name));
	char *t=name;
	printf("Size of t is %d\n",sizeof(t));
	int a[3];
	for(int i=0;i<3;i++){
		a[i]=i;
	}
	printf("size of %d is %i and address is %p",*a,sizeof(a),a);
	return 0;
}