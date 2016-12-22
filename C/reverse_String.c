#include <stdio.h>
#include <string.h>
void reverse_String(char  *s){
int len = strlen(s);
char *t = s + len -1;
while(t>=s){
	printf("%c",*t);
	t=t-1;
}
}
int main(){
char * name="Niranjan";
printf("%s\n",name);
reverse_String(name);
}