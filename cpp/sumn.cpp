#include <iostream>
using namespace std;
int main()
{
	int n,sum;
	int i=0;
	n=0;
	sum=0;
 	cin>>n;
	while(i<n)
	{
	sum+=i;
	++i;	
	}
	cout<<"sum is "<<sum<<endl;
}
