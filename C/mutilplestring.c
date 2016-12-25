#include<stdio.h>
#include<string.h>
int main() 
{
char songs[4][10]={"One Love","Blue","Tonight","Sugar"};
for(int i=0;i<4;i++){
	printf("%d",strstr(songs[i],"Love"));
}
}