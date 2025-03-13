def oddeven(number):
    if(number^1==number+1):
        return True
    else:
        return False
    
number=int(input("Enter number: "))
if oddeven(number):
    print(number,"is even")
else:
    print(number,"is odd")