#include <stdio.h>
int main() {
int start=0;
float latitude;
float longitude;
char info[80];
printf("[\n");
while(scanf("%f,%f,%79s[^c]",&latitude,&longitude,info)==3){
	if (start)
	printf(",\n");
	else
		start=1;
	if(latitude > 90.0 || latitude<-90.0 || longitude>180.0 || longitude < -180.0)
			fprintf(stderr,"This is invalid latitude:%f or longitude:%f\n",latitude,longitude);
	else
		printf("{latitude=%f,longitude=%f,info=%s}",latitude,longitude,info);
}
printf("\n]");
}