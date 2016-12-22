#include<stdio.h>
int main(){
	int a;
	long b;
	long long c;
	char d;
	char e[10];
	double g;
	float f;
	scanf("%d %ld %lld %c %9s %f %lf",&a,&b,&c,&d,e,&f,&g);
	printf("%d %ld %lld %c %9s %f %lf",a,b,c,d,e,f,g);
}