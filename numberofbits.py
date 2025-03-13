def numberofbits(number):
    count=0
    while(number):
        count+=1
        number>>=1 #number=number>>1
    return count
number=int(input("Enter a number: "))
print("Total number of bits=",numberofbits(number))