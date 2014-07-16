#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

int main()
{
int n,i,j,count[26];
bool found[26];
char a[200];
cin>>n;
i=0;
int ntemp=n;
for(i=0;i<26;i++)
count[i]=0;
while(n>0)
{
for(j=0;j<26;j++)
found[j]=false;
cin>>a;
for(j=0;j<strlen(a);j++)
{
found[a[j]-'a']=true;

}
for(j=0;j<26;j++)
{
if(found[j]==true)
{
count[j]++;
}
}
n--;
}
int co=0;
for(i=0;i<26;i++)
{
//cout<<count[i];
if(count[i]==ntemp)
{
co++;
}
}
cout<<co;
//cout<<minx;
//for(i=0;i<strlen())
}
