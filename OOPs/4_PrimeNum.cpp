// Wap to fid the prime numbers between 1 to 100.
#include <iostream>
using namespace std;

int main() {
    cout << "Prime numbers between 1 and 100 are:" << endl;

    // Loop through numbers from 2 to 100
    for (int num = 2; num <= 100; num++) {
        bool isPrime = true;

        // Check if 'num' is divisible by any number from 2 to num/2
        for (int i = 2; i <= num / 2; i++) {
            if (num % i == 0) {
                isPrime = false;
                break;  // No need to check further if we find a divisor
            }
        }

        // If 'num' is prime, print it
        if (isPrime) {
            cout << num << " ";
        }
    }

    cout << endl;
    return 0;
}
