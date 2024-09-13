#include <iostream>
using namespace std;
// Fehrenheit to celcius and cdlcius to Fehrenheit
int main(){
  float F, C ,a;
cout<<"Which conversion do you want to Perform?\n 1.Fehrenheit to celcius \n 2.Celcius to Fehrenheit"<<endl;
cin>>a;
 if(a== 1){ // Fahrenheit to Celsius conversion
  cout << "Enter temperature in Fahrenheit: ";
  cin >> F;
  C = (F - 32) * 5/9;
  cout << "Temperature in Celsius: " << C << endl;}

 else if(a==2){ // Celsius to Fehrenheit conversion
  cout << "Enter temperature in Celsius: ";
  cin >> C;
  F = C * 9/5 + 32;
  cout << "Temperature in Fahrenheit: " << F << endl;}
  else{
    cout << "Invalid option. Please try again." << endl;
    return 1;  // Exit with an error code of 1.
  }
return 0;
}