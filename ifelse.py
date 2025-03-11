def Sum (i,j): 
    return i+j
def Sub(i,j): 
    return i-j
def Prod(i,j): 
    return i*j
def divide(i,j): 
    return i/j
i=int(input("Enter i val :"))
j=int(input("Enter j val :"))
while True: 
    result=int(input("Enter 1.sum,2.sub,3.prod,4.divide"))
    if result==1:
        print("Sum is:",Sum(i,j)) 
    elif result==2 : 
        print("Sub is:",Sub(i,j)) 
    elif result==3: 
        print("Prod is:",Prod(i,j)) 
    elif result==4: 
        print("Divide is:",divide(i,j)) 
    else : 
        print("1-4 only")
        continue
    dec = input("press y  tocontinue or n exit: ").lower()
    if dec == 'y': 
        continue
    else:
        break
print("Thank you!")