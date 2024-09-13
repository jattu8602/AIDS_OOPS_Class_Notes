# My C++ Programs

This repository contains a collection of basic C++ programs demonstrating various concepts. Each file is focused on a specific problem or calculation.

## Files and Contents

1. **HelloWorld**
   - A simple C++ program that prints "Hello, World!" to the console.

2. **Convert Fahrenheit to Celsius and Convert Celsius to Fahrenheit**
   - A program to convert temperatures between Fahrenheit and Celsius.
   - Formula for Fahrenheit to Celsius:
     ```cpp
     Celsius = (Fahrenheit - 32) * 5/9;
     ```
   - Formula for Celsius to Fahrenheit:
     ```cpp
     Fahrenheit = (Celsius * 9/5) + 32;
     ```

3. **WAP to Find the Area of a Circle**
   - This program calculates the area of a circle given the radius.
   - Formula used:
     ```cpp
     Area = π * r²;
     ```
   - `r` is the radius of the circle, and `π` is approximately `3.14159`.

4. **WAP to Print Prime Numbers Till 100**
   - This program prints all prime numbers between 1 and 100.
   - A prime number is a number greater than 1 that is divisible only by 1 and itself.

5. **WAP to Print Quotient and Remainder**
   - A program that calculates the quotient and remainder when dividing two integers.
   - Uses the division operator (`/`) for quotient and the modulo operator (`%`) for remainder.

## How to Compile and Run

You can compile any of these C++ programs using a C++ compiler like `g++`. Here's an example of how to compile and run the `HelloWorld` program:

```bash
g++ -o HelloWorld HelloWorld.cpp
./HelloWorld
