#!/usr/bin/python3
def fizzbuzz():
    """Prints the numbers from 1 to 100, Fizz for multiples of three, Buzz for
     multiples of five, FizzBuzz for multiples of both"""
    for n in range(1, 101):
        if n % 5 == 0 and n % 3 == 0:
            print("FizzBuzz ", end="")
        elif n % 5 == 0:
            print("Buzz ", end="")
        elif n % 3 == 0:
            print("Fizz ", end="")
        else:
            print(f"{n} ", end="")
