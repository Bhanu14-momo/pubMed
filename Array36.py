#Reverse an Array/String
"""arr=[1,4,2,3,6,5]
reverse_arr=arr[::-1]
print(reverse_arr)

#Find the maximum and minimum element in an array
def minmax(arr):
    max_num=arr[0]
    min_num=arr[0]
    for num in (arr):
        if  num >max_num:
            max_num=num
        if num<min_num:
            min_num=num
    return max_num,min_num
arr=[1,3,5,6,7,9]
max_val, min_val = minmax(arr)
print("Max:", max_val)
print("Min:", min_val)


#Sort an array of 0s, 1s and 2s - Dutch National Flag Problem
def sort012(n): 
    low=0
    high=len(n)-1
    i=0
    while (i<=high): 
        if n[i]==0: 
           n[i],n[low]=n[low],n[i]
           low+=1
           i+=1
        elif n[i]==2: 
            n[i],n[high]=n[high],n[i]
            high-=1
        else: 
            i+=1
n=[0,2,0,1,1,2,0,1,0]
sort012(n)
print(n)

#Move all the negative elements to one side of the array

def move_negatives(arr): 
    j=0
    for i in range(len(arr)): 
        if arr[i] < 0: 
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
move_negatives(arr)
print(arr)

#Armstrong Number Program in  python

n = int(input("Enter n value: "))
length = len(str(n))
temp = n
sum = 0

while temp > 0:
    digit = temp % 10  
    sum += digit ** length  
    temp //= 10  

print("Number is {} and calculated sum is {}".format(n, sum))

if n == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

#reverse each char

n=int(input("enter n value: "))
original_num=n
reverse_num=0
while n>0: 
    digit=n%10
    reverse_num=reverse_num*10+digit
    n//=10
print("The reverse_num  {} is {}".format(original_num,reverse_num))

#How to Find All Substrings of a Given String 

def substring(str1, n): 
    substrings = []  
    for i in range(n): 
        for j in range(i + 1, n + 1): 
            substrings.append(str1[i:j]) 
    return substrings

str1 = 'Bhanu'
n = len(str1)
res = substring(str1, n)

print("All substrings of '{}':".format(str1))
for s in res:
    print(s)

#How to Remove Duplicate Elements from an Array 

def removedupl(lst1): 
    noduplicates=[]
    for ele in lst1: 
        if ele not in noduplicates: 
            noduplicates.append(ele)
    return noduplicates
lst1=[40,80,80,90,60,50,40,30]
lst1.sort()
res=removedupl(lst1)
print(res)

#How to Remove Duplicate Characters from a String 

def removeduplstr(str):
    noduplstr=[] 
    for char in str: 
        if char not in noduplstr: 
            noduplstr.append(char)
    st=" ".join(noduplstr)
    return st
str='Bhaaaaanuuuuu'
res=removeduplstr(str)
print(res)

# How to Perform Left Circular Rotation of an Array. 

def leftrotation(arr,shift): 
    for i in range(shift): 
        temp=arr[0]
        for j in range(len(arr)-1):
            arr[j]=arr[j+1]
        arr[-1]=temp
    return arr
arr=[1,2,3,4,5]
shift=3
print(f"Before rotation {arr}")
res=leftrotation(arr,shift)
print("\n After rotation: ")
print(res)

#How to Perform Right Circular Rotation of an Array 

def rightrotation(arr,shift): 
    for i in range(shift): 
        temp=arr[-1]
        for j in range(len(arr)-1,0,-1):
            arr[j]=arr[j-1]
        arr[0]=temp
    return arr
arr=[1,2,3,4,5]
shift=2
print(f"Before rotation {arr}")
res=rightrotation(arr,shift)
print("\n After rotation: ")
print(res)

#How to convert a two-dimensional array to one-dimensional array.
from numpy import *
a=array([[1,2,3],[4,5,6],[2,3,4]])
b=a.flatten()
print(b.ndim)
print(a.shape)
print(b)

#How to convert a one-dimensional array to a two-dimensional array.
from numpy import *
a=array([1,2,3,4,5,6])
b=a.reshape(2,3)
print(b.ndim)
print(b.shape)
print(b)


#sum of digits
n = int(input("Enter a number: "))
sum_of_digits=0
while n>0:
    digit=n%10
    sum_of_digits+=digit
    n//=10
print("The sum of digits :" ,sum_of_digits)

#Move all Zeroes to end: 

lst1=[0,1,0,2,0,0,5,6,0,0,33,66,77]
lst2=[]
lst3=[]
for i in lst1: 
    if i==0: 
        lst2.append(i)
    else: 
        lst3.append(i)
        lst3.sort()
    lst4=lst3+lst2
print("Move Zero to end :",lst4)

#Find the second largest number:  

lst=[2,3,1,4,5]
largest=second_largest=float('-inf')
for num in lst: 
    if num>largest:   #num=2 largest=-inf   2>-inf :True   second_largest=largest,largest=num-->(2)
        second_largest=largest 
        largest=num
    elif num>second_largest and num!=largest :   
        second_largest=num
print("The Second_largest number is: ",second_largest)


#find kth smallest element: 

lst = [2, 5, 3, 7, 10, 15]
k = 2
for num in range(k): 
    smallest=float('inf')
    for num in lst: 
        if num<smallest:
            smallest=num
    lst.remove(smallest) 
kth_smallest=smallest
print("The Kth smallest ele is : ",smallest)

#find kth largest element : 

lst = [12,3,5,7,19]
k = 2
for num in range(k): 
    largest=float('-inf')
    for num in lst: 
        if num>largest:
            largest=num
    lst.remove(largest) 
kth_largest=largest
print("The Kth largest ele is : ",largest)

#find the missing number  in a sequence : 

def missing_num(num): 
    n=len(num)+1
    total_sum=n*(n+1)//2
    actual_sum=sum(num)
    missing_num=total_sum-actual_sum
    return missing_num
lst=[1,2,3,4,6]
print("The missing number is:",missing_num(lst))

#Check if a String is a Palindrome

def pallindrome(s):
    left=0
    right=len(s)-1
    if left<right:
        while left<right and not s[left].isalnum():
            left+=1
        while left<right and  not s[right].isalnum():
            right-=1
        while s[left].lower()!=s[right].lower():
            return False
        left+=1
        right-=1
    return True
s='madam'
res=pallindrome(s)
print("The s is  pallindrome : ",res)

# Find Duplicates in an Array

lst = [10, 20, 10, 30, 20, 40, 50]
unique = []

for i in range(len(lst)):
    count = 0
    for j in range(len(lst)):
        if lst[i] == lst[j]:
            count += 1
    if count > 1 and lst[i] not in unique:
        unique.append(lst[i])

print(unique)

# Check if an Array is Sorted

def issorted(arr): 
    for i in range(len(arr)-1): 
        if arr[i]>arr[i+1]: 
            return False
    return True
lst=[1,2,3,4,5]
res=issorted(lst)
print(res)

#Find the Largest Sum Contiguous Subarray (Kadane’s Algorithm)

lst= [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum=float('-inf')
curr_sum=0
for num in lst:
    curr_sum=max(num,curr_sum+num)
    max_sum=max(max_sum,curr_sum)
print(max_sum)

# Count Frequency of Elements in an Array

lst=[1,2,2,3,3,4]
count={}
for num in lst:
    if num in count:
        count[num]+=1
    else:
        count[num]=1
print(count)

# Find the Intersection of Two Arrays
lst1=[1,2,2,3]
lst2=[2,3,4]
lst3=[]
for num in lst1: 
    if num in lst2: 
        lst3.append(num)
        lst2.remove(num)
print(lst3)

#Check if a Number is a Power of Two

n=int(input("Enter from user: "))
if n>0 and (n&(n-1))==0:
    print(True)
else:
    print(False)


# Find the Longest Substring Without Repeating Characters

def longsubstr(s): 
    res=set()
    start=0
    max_len=0
    for end in range(len(s)): 
        while s[end] in res: 
            res.remove(s[start])
            start+=1
        res.add(s[end])
        max_len=max(max_len,end-start+1)
    return max_len
s="abcabcbb"
output=longsubstr(s)
print("The logest sub str is :",output)

#Find the Union of Two Arrays

lst1=[1, 2, 3, 4]
lst2=[3, 4, 5, 6]
lst3=list(set(lst1+lst2))
print(lst3)


#Implement binary search on a sorted array to find an element.

def binarysearch(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left+=1
        else:
            right-1
    return -1
arr=[1, 3, 5, 7, 9]
target = 5
res= binarysearch(arr,target)
print("The index of the element 5 is : ",res)

#twosum

def twosum(arr,target): 
    left=0
    right=len(arr)-1
    while left<right: 
        curr_val=arr[left]+arr[right]
        if curr_val==target: 
            return [left,right]
        elif curr_val<target: 
            left+=1
        else: 
            right-=1
    return -1
arr=[3,4,5,7,9,11]
target=18
res=twosum(arr,target)
print("The indicies of 12 is: ",res)

#  Find the Majority Element Given an array, find the element that appears more than n//2 times (if any).

def majorityele(arr): 
    freq={}
    n=len(arr)
    for num in arr: 
        freq[num]=freq.get(num,0)+1
        if freq[num]>n//2: 
            return num
    return -1
arr=[3, 3, 4, 2, 4, 4, 2, 4, 4]
res=majorityele(arr)
print("The majority ele is : ",res)

#Find the Longest Common Prefix in an Array of Strings

s=["flower", "flow", "flight"]
ans=""
s.sort()
for i in range(len(s[0])): 
    if s[0][i]==s[-1][i]: 
        ans+=s[0][i]
    else: 
        break
print("The longest common prefix is: ",ans)

# Check for Balanced Parentheses

def is_balanced(s): 
    l=[]
    d={'(':')','[':']','{':'}'}
    for i in s: 
        if i in d: 
            l.append(i)
        elif i in d.values(): 
            x=l.pop() if l else '#'
            if d.get(x)!=i:
                return False
    return not l
s = "() [] {}"
if is_balanced(s):
    print(True)
else:
    print(False)


#Find the Peak Element

def find_peak_binary(arr): 
    left=0
    right=len(arr)-1
    while left<right: 
        mid=(left+right)//2
        if arr[mid]<arr[mid+1]: 
            left=mid+1
        else: 
            right=mid
    return arr[left]
arr=[1, 3, 20, 4, 1, 0]
res=find_peak_binary(arr)
print("Peak Element is:",res)

#Count the Number of Occurrences of an Element
def count_occurance_ele(arr): 
    count=0
    for num in arr: 
        if num==ele: 
            count+=1
    return count
arr=[1, 2, 2, 3, 2, 4, 5]
ele=2
res=count_occurance_ele(arr)
print(f'Count the Number of Occurrences of an Element {ele} is: ',res)

#Find the Element that Appears Once in an Array

def find_single_element(arr):
    unique=0
    for num in arr: 
        unique^=num
    return unique
arr=[2, 2, 3, 3, 4, 5, 5]
res=find_single_element(arr)
print(f'The element that Appears Once in an Array: ',res)

#Longest Consecutive Sequence
def longestseq(nums): 
    largest=0
    num=set(nums)
    for i in num: 
        if i-1 not in num: 
            length=1
            while i +length in num: 
                length+=1
            largest=max(largest,length)
    return largest
nums=[100,4,200,1,2,3]
res=longestseq(nums)
print("The longest seq is :",res)

#Find the Subarray with a Given Sum

arr=[1, 2, 3, 7, 5]
s=12
def subarrsum(arr,s): 
    res=[]
    for i in range(len(arr)): 
        res.append(arr[i])
        while (sum(res)>s): 
            res.pop(0)
        if sum(res)==s: 
            return res
    return []
print(subarrsum(arr,s))

#Find the Majority Element Using Boyer-Moore Voting Algorithm
nums=[3, 3, 4, 2, 4, 4, 2, 4, 4]
def majorityele(nums): 
    candidate=None
    count=0
    for num in nums: 
        if count==0: 
            candidate=num
        count+=1 if num==candidate else-1 
    if nums.count(candidate)>len(nums)//2:
        return candidate
    else: 
        return None
print( majorityele(nums))


#largest prime factor
n=56
def largest_prime_factor(n):
    i=2
    while i*i<=n:
        if n%i==0:
            n//=i
        else:
            i+=1
    return n
print(largest_prime_factor(n))

#Find the GCD of Two Numbers

a=56
b=98
def Gcd(a,b): 
    while b!=0: 
        a,b=b,a%b
    return a
print("The greatest Common divisor is: ",Gcd(a,b))

#Merged two sorted arr

arr1=[1, 3, 5]
arr2=[2, 4, 6]
def merge_sorted_arr(arr1,arr2):
    res=[]
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
    while i<len(arr1):
        res.append(arr1[i])
        i+=1
    while j<len(arr2):
        res.append(arr2[j])
        j+=1
    return res
print("The merged_sorted arr:" ,merge_sorted_arr(arr1,arr2))

#longest pallindrome substrings

def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) < 1:
        return ""

    longest = ""
    for i in range(len(s)):
        odd_palindrome = expand_around_center(i, i)
        even_palindrome = expand_around_center(i, i + 1)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        if len(even_palindrome) > len(longest):
            longest = even_palindrome

    return longest

s = "babad"
print("Longest Palindromic Substring:", longest_palindrome(s))


#Flatten a List of Lists

lst1= [[1, 2], [3, 4], [5, 6]]
lst2= [item for sublist in lst1 for item in sublist]
print(lst2)

#sum of_digits

def sum_of_digits(n): 
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    return sum
n=123456
print("The sum of digits : ",sum_of_digits(n))

# Find All Prime Numbers Less Than N (Sieve of Eratosthenes)
n=30
def Sieve_Eratosthenes(n): 
    if n<2: 
        return []
    is_prime=[True]*n
    is_prime[0]=is_prime[1]=False
    for i in range(2,int(n**0.5)+1): 
        if is_prime[i]: 
            for j in range(i*i,n,i): 
                is_prime[j]=False
    primes=[i for i in range(n) if is_prime[i]]
    return primes
print("All Prime Numbers Less Than N ",n ,"is :",Sieve_Eratosthenes(n))

#Identicaltwins

from collections import defaultdict
def findduplele(arr):
    dupl = 0
    count = defaultdict (list)
    for i, num in enumerate(arr):
        if num in count:
           dupl+=len(count[num])
        count[num].append(i)
    return dupl
arr = [1, 2, 3, 2, 1]
print("The number of identical twins: ",findduplele(arr))

#method 2

def findduplele(arr):
    count= set()
    dupl = set()
    
    for num in arr:
        if num in count:
            dupl.add(num)
        else:
            count.add(num)
    
    return  len(dupl)

arr = [1, 2, 3, 2, 1]
print("Number of Duplicates: ",findduplele(arr))

# Rotate a Matrix (90 Degrees Clockwise)Problem: Rotate an n x n matrix 90 degrees clockwise.

matrix=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def rotate_matrix(matrix): 
    n=len(matrix)
    for i in range(n): 
        for j in range(i,n): 
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for row in matrix: 
        row.reverse()
    return matrix
rotated_matrix=rotate_matrix(matrix)
for row in rotated_matrix: 
    print(row)


#find longest  increasing sub sequence: 

arr=[10, 22, 9, 33, 21, 50, 41, 60, 80]
def longestsubseq(arr): 
    if not arr: 
        return 0
    n=len(arr)
    dp=[1]*n
    for i in range(1,n): 
        for j in range(i): 
            if arr[i]>arr[j]: 
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)
print("The longest sub sequence is : ",longestsubseq(arr))

#Find the First Non-Repeating Character in a String

s="leetcode"
def noduplchar(s):
    s1={}
    for char in s:
        s1[char]=s1.get(char,0)+1
    for char in s: 
        if s1[char]==1:
            return (char)
    return -1
print(noduplchar(s))

#Check if a String is a Valid Number (Integer/Float)

def checkValid(num): 
    try:    #error might occurs.
        float(num)  #convert num into float.
        return True
    except ValueError:   #catch valueerrors.
        return False
num=input("Enter from User: ")
print(checkValid(num))

#Find All Anagrams in a String

def findAnagrams(s,p): 
    res=[]
    if len(p)>len(s):  #p>s
        return []
    sCount,pCount={},{}  #freqs,freqp
    for i in range(len(p)):  #len(p)=3
        sCount[s[i]]=sCount.get(s[i],0)+1 #freq get ele not 0
        pCount[p[i]]=pCount.get(p[i],0)+1 #freq get ele not 0
        if sCount==pCount:  #s{c:1,b:1,a:1},p{a:1,b:1,c:1}
            res.append(0)   #res=[0]
    l=0       #l=c
    for r in range(len(p),len(s)):  #right pointer len(p),len(s)
        sCount[s[r]]=sCount.get(s[r],0)+1  #freq of r if present 1 not 0
        sCount[s[l]] -= 1  # Remove leftmost character


        if sCount[s[l]]==0:  #s{c:1-1=0,b:1,a:1}
            del sCount[s[l]]  #s{b:1,a:1}
        l+=1  #s{b:1,a:1,e:1}
        if sCount==pCount: 
            res.append(l)  # Append the starting index of anagram
    return res
s="cbaebabacd"
p="abc"
print(findAnagrams(s,p))

#kth largest mtd2: 

def kth_largest(arr,k):
    arr.sort(reverse=True)
    return arr[k-1]
arr=[10,2,4,6,7,3,8]
k=2
print(kth_largest(arr,k))

#kth smallest mtd2: 

def kth_smallest(arr,k):
    arr.sort()
    return arr[k-1]
arr=[10,2,4,6,7,3,8]
k=2
print(kth_smallest(arr,k))

#prime seq mtd2: 
n=20
def primes(n):
    seq=[]
    for num in range(2,n+1):
        isprime=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                isprime=False
                break
        if isprime:
            seq.append(num)
    return seq
print(primes(n))"""


    
    
    







    



    


        


