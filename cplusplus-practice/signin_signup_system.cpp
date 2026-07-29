#include<iostream>
#include<stdlib.h> // TO USE EXIT FUNCTION FOR SUCCESSFUL TERMINATION
#include<string.h> // TO USE STRING DATATYPE
using namespace std;
int userChoice;
void firstPage(userChoice);
int main()
{
	char quit;
	int maxAttemp=3;
	string name,userName ,pass,userPass,tempUserName,tempName,tempPass;
	while(quit != 'y')
{
	cout<<"Welcome back to Number Guessing Game :)"<<endl;
	cout<<"Please login or Create a new Account to countinue !"<<endl;
	cout<<"1. Login \n2. Create a Account"<<endl;
	cout<<"3. Reset or Forget your password. \n4. Exit"<<endl;
	cout<<"Enter your choice : ";
	cin>>userChoice;
	firstPage(userChoice);
	cout<<"Do you want to quit ? (Press 'y' to quit.) ";
	cin>>quit;
	cout<<"\n******************************\n";
}
	return 0;
}

void firstPage(userChoice)
{
	if(userChoice == 1)
		{
			for(int i=1; i<= maxAttemp; i++)
			{
			cout<<"Enter User Name : ";
			cin>>name;
			cout<<"Enter your Password : ";
			cin>>userPass;
			if (userPass == pass)
			{
				cout<<"Main Menu : \n1.Easy Level (1-10)"<<endl;
				cout<<"2. Medium Level (1-50) \n3. Hard Level (1-100)"<<endl;
				cout<<"4. Check Your Score \n5. Remaining Tokens"<<endl;
				cout<<"6. Recharge Your Tokens \n7. Withdarw Your Earning"<<endl;
				cout<<"8. Exit"<<endl;
				cout<<"\n New Code here."<<endl;
			}
			else
			{
				if( i == maxAttemp)
				{
					cout<<"You have reached maximum limits."<<endl;
					cout<<"Your Account have been blocked."<<endl;
					cout<<"Reset your password to countinue."<<endl;
				}
				else
				{
				cout<<"The password you entering is wrong. Try Again!"<<endl;	
			}
			}
		}
			continue;
	}
		else if (userChoice == 2)
		{
			cout<<"Enter your Name : ";
			cin>>name;
			userName = name+string("@game.pk");
			cout<<"Enter a Strong Password : ";
			cin>>pass;
			cout<<"Your User Name = "<<userName<<endl;
			cout<<"Your Password = "<<pass<<endl;
			cout<<"Rember this for future use."<<endl;
			continue;
	}
		else if (userChoice == 3)
		{
			for(int i = 1; i<= maxAttemp; i++)
			{
			cout<<"Enter user name : ";
			cin>>tempUserName;
			cout<<"Enter your name given at the time of account creation : ";
			cin>>tempName;
			if(tempName.compare(name) == 0 && tempUserName.compare(userName) == 0)
			{
				cout<<"Access granted."<<endl;
				cout<<"Enetr new password : ";
				cin>>tempPass;
				pass = tempPass;
				cout<<"Your new password = "<<pass<<endl;
				continue;
			}
			else
			{
				if (i == 3)
				{
					cout<<"Your account is permanantely blocked."<<endl;
					cout<<"You can create new account to access the game."<<endl;
				}
				else
				{
				cout<<"Username or Name is wrong."<<endl;
				}
			}
		}
				break;
	}
		else if(userChoice == 4)
		{
			cout<<"Closing the program...";
			continue;
	}
		else {
				cout<<"Invalid input. Please enter from 1 to 4.";
				continue;
		}
}