"""lst=[]
for i in range(1,11): 
    if i!=0: 
        lst.append(i)    
print(lst)

#sum of 2 nums
n1=int(input("enter n1 val :"))
n2=int(input("enter n2 val :"))
def sum(n1,n2): 
    return n1+n2
sum(n1,n2)
print("The Sum Of n1+n2 : ",sum(n1,n2))

#even odd 
def evenodd(num): 
    if num%2==0: 
        print(f'The {num} is Even')
    else: 
        print(f'The {num} is Odd ')
num=int(input("Enter Num Val : "))
evenodd(num)

# factorial of a number
def fact(n): 
    if n==0 or n==1: 
        return n
    else: 
        return n*fact(n-1)
n=int(input("Enter n Val : "))
print(f'The  factorial of a {n} : ',fact(n))

#Reverse a string entered by the user.

str=input("Enter str Val : ")
reverse_str=str[::-1]
print("Reverse str : ",reverse_str)

#Write a program to check if a year is a leap year.
year=int(input("Enter a year : "))
if ((year%4==0 and year%100!=0)or(year%400==0)): 
    print(f'The {year} is a leapyear')
else: 
    print(f'The year is not a leapyear')

#Find the largest of three numbers.
n1=float(input("Enter n1 Val :"))
n2=float(input("Enter n2 Val :"))
n3=float(input("Enter n3 Val :"))
print(f'The max value of n1,n2,n3 is ',max(n1,n2,n3))

#Create a simple calculator (add, subtract, multiply, divide).
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

#Write a program to swap two numbers without using a temporary variable.

n1=int(input("nter n1 val : "))
n2=int(input("nter n2 val : "))
print(f'Before swap a={n1} and b={n2}')
n1,n2=n2,n1
print(f'After swap a={n1} and b={n2}')"""

#Print the first N natural numbers.
n=int(input("enter n val : "))
for i in range(1,n+1): 
    print(i, end=" ")






