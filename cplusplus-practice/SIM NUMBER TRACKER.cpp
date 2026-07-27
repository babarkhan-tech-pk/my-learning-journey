#include<iostream>
using namespace std;
int simNumberTracker();
int main()
{
	simNumberTracker();
	return 0;
}
simNumberTracker()
{
	long long num;
	int comp , i , arr[10] = {};
	cout<<"Enter your phone number without first 0 (ex. 3012345678) : ";
	cin>>num;
	if (num > 3000000000 && num < 3999999999)
	{
		cout<<"You enter a correct number."<<endl;
		cout<<"Processing ..."<<endl;
		for( i = 0 ; i < 10 ; i++)
		{
			arr[i] = num % 10;
			num = num / 10;
		}
		for(i = 9 ; i >= 0 ; i--)
		{
			cout<<"Digit "<<i+1<<" = "<<arr[i]<<endl;
		}
		comp = ( arr[9] * 100 ) + ( arr[8] * 10 ) + arr[7];
		cout<<"Company code = "<<comp<<endl;
		if( (comp >= 300 && comp <= 309) || (comp >= 320 && comp <= 329))
		{
			cout<<"This mobile number company is Jazz."<<endl;
		}
		else if ( (comp >= 310 && comp <= 319) || (comp >= 370 && comp <= 379))
		{
			cout<<"This mobile number company is Zong."<<endl;
		}
		else if ( comp >= 340 && comp <= 349)
		{
			cout<<"This mobile number company is Telenor."<<endl;
		}
		else if ( comp >= 330 && comp <= 339)
		{
			cout<<"This mobile number company is UFone."<<endl;
		}
		else
		{
			cout<<"Invalid number. Company does not exist in Pakistan."<<endl;
		}
	}
	else
	{
		cout<<"Invalid input. Please enter a valid 10 digit number."<<endl;
	}
	return 0;
}