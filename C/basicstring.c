#include<stdio.h>
int main()
{
char name[20];
scanf("%s",&name);
printf("%s",name);
fgets(name,sizeof(name),stdin);
printf("%s",name);
}