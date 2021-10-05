//header files
#include <bits/stdc++.h>
#include <fstream>
#include<string>
using namespace std;

/*
this function add student record to text file
Argument1: filename
Argument2: Pointer to studentCount
*/
void addStudent(string filename, int *studentCount, int *inStateFees, int *outStateFees){
cout<<endl<<"Press any key to add Students details";
getchar();
ofstream file(filename.c_str(), ios::app);
char name[50];
cout<<endl<<"\n Enter Name of Student : ";
cin>>name;

file<<endl<<name;

int state=-1;
cout<<endl<<"\n Press 1 for In-State or 2 for Out-Of-State : ";
cin>>state;

if(state==1)
file<<" | In-State";
else if(state==2)
file<<" | Out-Of-State";
else
file<<" | NA";

int tutionFees;
cout<<endl<<"Enter Tution Fees : ";
cin>>tutionFees;

char choice;
cout<<endl<<"Do you want to enroll for Health Plan ? y/n : ";
cin>>choice;

int healthPlan = 0;

if(choice=='Y' || choice=='y'){
char plan;
cout<<endl<<" # Select Optional Health Plan #";
cout<<endl<<"E -> $40";
cout<<endl<<"S -> $160";
cout<<endl<<"C -> $120";
cout<<endl<<"F -> $200";

cout<<endl<<"Select any alphabet ( E, S, C, F ) : ";
cin>>plan;

switch(plan){     	
case 'E':
case 'e': healthPlan = 40;   break;
case 'S':
case 's': healthPlan = 160; break;
case 'C':
case 'c': healthPlan =  120; break;
case 'F':
case 'f' : healthPlan =  200; break;
default: cout<<endl<<"Invalid Choice..";
}

if(healthPlan!=0)
file<<" | Health Plan : "<<plan;
else
file<<" | Health Plan : None"<<plan;

file<<" | "<<tutionFees;

if(state==1){
*inStateFees = *inStateFees + tutionFees + healthPlan;
}
else if(state==2){
*outStateFees = *outStateFees + tutionFees + healthPlan;
}

}
*studentCount = *studentCount + 1;
file.close();
}

/*
function generate the final report by adding total fees details
Argument1: filename
Argument2: Pointer to studnetCount
*/
void generateReport(const string filename, const int *studentCount, const int *inStateFees, const int *outStateFees){
if(*studentCount==0){
cout<<endl<<"Error: There should be atleast one record to generate report.";
}
else{
ofstream file(filename.c_str(), ios::app);
file<<endl<<"Total Tuition Paid for all In-State Students : "<<*inStateFees;
file<<endl<<"Total Tuition Paid for all Out-of-State Students : "<<*outStateFees;
file.close();
cout<<endl<<"Success: "<<filename<<" generated ";		
}
	
}


//program runs from this function
int main(int argc, char** argv) {
	
int choice = 0;
string fileName = "tuition_report.txt";
int studentCount =0;
int inStateFees = 0;
int outStateFees =0;

//empty file if it already exist
ofstream file(fileName.c_str(), ios::out);
file.close();

while(choice!=-1){
cout<<endl<<"## (College Student Tuition) ##"<<endl;
cout<<endl<<"1 Add Student Details";
cout<<endl<<"2 Generate Report";
cout<<endl<<"-1 Exit";
cout<<"\n\n Enter your choice : ";
cin>>choice;

switch(choice){
case 1: addStudent(fileName, &studentCount, &inStateFees, &outStateFees);
	break;
case 2: generateReport(fileName, &studentCount, &inStateFees, &outStateFees);
	break;
case -1: cout<<endl<<"thank you for useing softwer!!";
	break;
default: cout<<endl<<"Invalid Choice.."; getchar();
	
}
	
}

return 0;
}
