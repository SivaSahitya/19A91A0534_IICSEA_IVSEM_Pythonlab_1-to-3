#3.3)Implement a python script that prompts the user for a number, and prints that number in words. 
num={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero'};
length=[]
i=int(input("Enter a number :"))
n=i
while n!= 0:
    r=n%10
    length.append(r)
    n=n//10
length.reverse()
for i in length:
    print(num[i],end=" ")

    """output:
    Enter a number :10
    one zero  
    Enter a number :234
    two three four 
    
    
