#2.2)Implement a python script add.py that takes 2 numbers as command line arguments and perform arithmetic operations on them.
import sys 
a=int(input(sys.argv[1]))#sys.argv-It returns a list of command line arguments passed to a python script
b=int(input(sys.argv[2]))
c=a+b 
print('sum is: ',c)

"""output:
          3
          2
          sum is:  5
