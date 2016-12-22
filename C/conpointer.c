#include <stdio.h>
int main() {
char name[5]="Life";
char *aname=name;
name[0]='D';
name[1]='e';
name[2]='a';
name[3]='d';
printf("%s %s", name,aname);
}