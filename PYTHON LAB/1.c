#include<stdio.h>
int main(){
	int n;
	int flag=0;
	scanf("%d",&n);

	for(int i=0;i<=n;i++)
	{
		if(n%i==0)
		{
			for(int j=2;j<i;j++) 8   
			{
				if(i%j==0)
				{
					flag=1;
					break;
				}
			}
			if(flag==0)
			{
				printf("%d ",i);
			}
		}

	}
}