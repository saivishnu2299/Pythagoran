def menu():
    #print the options you have
    print "Welcome to Pythagorean Theorem Calculator.py"
    print "Please keep in mind that for this program to work you need the length of two side of the triangle"
    print " "
    print "Your Options Are:"
    print " "
    print "1) If you have the length of A and B"
    print " "
    print "2) If you have the length of C and A"
    print " "
    print "3) If you have the length of C and B"
    print " "
    print "4) Quit Pythagorean Theorem Calculator.py"
    print " "
    return input ("Choose your option: ")

from math import *

#On this one we have the length of A and B and we are trying to find the length of C
def AnB(a,b):
    print a**2, "+", b**2, "=", a**2 + b**2
    print sqrt(a**2 + b**2)

#On this one we have the length of A and C and we are trying to find the length of B
def CnA(c,a):
    print c**2, "-", a**2, "=", c**2 - a**2
    print sqrt(c**2 - a**2)

#On this one we have the length of B and C and we are trying to find the length of A
def CnB(c,b):
    print c**2, "-", b**2, "=", c**2 - b**2
    print sqrt(c**2 - b**2)

# NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        AnB(input("A: "),input("B: "))
    elif choice == 2:
        CnA(input("C: "),input("A: "))
    elif choice == 3:
        CnB(input("C: "),input("B: "))
    elif choice == 4:
        loop = 0

print "Thank you for using Pythagorean Theorem Calculator.py"
