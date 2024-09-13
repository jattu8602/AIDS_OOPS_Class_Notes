#include <iostream>
using namespace std;

int main() {
    int dividend, divisor;

    // Taking input from the user
    cout << "Enter the dividend: ";
    cin >> dividend;
    cout << "Enter the divisor: ";
    cin >> divisor;

    // Calculating quotient and remainder
    int quotient = dividend / divisor;
    int remainder = dividend % divisor;

    // Displaying the results
    cout << "Quotient: " << quotient << ", Remainder: " << remainder << endl;
    return 0;
}
