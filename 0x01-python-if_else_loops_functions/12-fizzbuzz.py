#!/usr/bin/python3


def fizzbuzz():

    x = 1

    while x <= 100:
        if (x % 5) == 0 and (x % 3) == 0:
            print("FizzBuzz ", end="")

        elif (x % 3) == 0:
            print("Fizz ", end="")

        elif (x % 5) == 0:
            print("Buzz ", end="")

        else:
            print("{} ".format(x), end="")

        x += 1

    print()
