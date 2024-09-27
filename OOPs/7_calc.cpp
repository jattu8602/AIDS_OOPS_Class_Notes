// wap in c++ to make a calculator of arithmetic operations
#include <iostream>
using namespace std;

int main(){
// also add modulus to it and use if else statements
int a, b, c;
cout<<"Enter two numbers: ";
cin>>a>>b;
cout<<"Enter the operation (+,-,*,/,%): ";
char op;
cin>>op;
// use if else statements
lb;
if(op=='+'){
  c = a + b;
  cout<<"The sum is: "<<c<<endl;
}
else if(op=='-'){
  c = a - b;
  cout<<"The difference is: "<<c<<endl;
}
else if(op=='*'){
  c = a * b;
  cout<<"The product is: "<<c<<endl;
}
else if(op=='/'){
  if(b==0){
    cout<<"Error: Division by zero is not allowed."<<endl;
  }
  else{
    c = a / b;
    cout<<"The quotient is: "<<c<<endl;
  }
}
else if(op=='%'){
  if(b==0){
    cout<<"Error: Division by zero is not allowed."<<endl;

  }
  else{
    c = a % b;
    cout<<"The remainder is: "<<c<<endl;
  }
}

  else{
    cout<<"Invalid operator. Please use (+,-,*,/,%)"<<endl;
    

  }








return 0;
}