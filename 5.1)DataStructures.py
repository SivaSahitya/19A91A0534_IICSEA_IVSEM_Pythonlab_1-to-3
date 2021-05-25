#5.1)Implement a python script to count frequency of characters in a given string
o=input('Enter a string as input:')
p={} #{} are used to define a dictionary
for i in set(o):
    p[i]=o.count(i) #count() function returns the number of occurrences of a substring in the given string
print(p)

"""output:Enter a string as input:aditya
{'y': 1, 'a': 2, 'd': 1, 't': 1, 'i': 1}"""
