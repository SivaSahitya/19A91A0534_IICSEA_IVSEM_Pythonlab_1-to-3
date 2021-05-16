#1.2)Implement a python script to purposefully raise Indentation Error and Correct it.
if a>b:
print('a is greater')
output:
IndentationError: expected an indented block
    
#correction of a indentation error
a=5
b=1
if a>b:
  print("a is great")
output:
a is great

>>> a=10
>>>   b=20
>>>print(a,b)
output:
IndentationError: unexpected indent
  
#correction of indentation error
>>> a=10
>>> b=20
>>> print(a,b)
10 20
