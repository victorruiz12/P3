
import os
import sys

#class
class Lab3:
    def py1(self):
        os.system("python 1.py")
    def py2(self):
        os.system("python 2.py")
    def py3(self):
        os.system("python 3.py")
    def py4(self):
        os.system("python 4.py")

election = Lab3()

def choice():
    print("\n Make a choice")
    print("\n1: Ex 1")
    print("\n2: Ex 2")
    print("\n3: Ex 3")
    print("\n4: Ex 4")
    print("\n0: Exit")
    x = input()
    return x

while (True):
    x = choice()
    if x == "1":
        election.py1()
    elif x == "2":
        election.py2()
    elif x == "3":
        election.py3()
    elif x == "4":
        election.py4()
    elif x == "0":
        sys.exit()