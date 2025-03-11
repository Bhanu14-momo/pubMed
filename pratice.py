# remove duplicates:
"""arr=[1, 2, 2, 3, 4, 4, 5]
def dupl(arr):
    res=[]
    for i in arr:
        if i  not in res: #i! in res
            res.append(i)
    return res
print(dupl(arr))"""

#Move Zeroes To End:
"""lst1=[0, 1, 2, 0, 3, 4]
lst2=[]
lst3=[]
for i in lst1:
    if i==0:
        lst2.append(i)
    else:
        lst3.append(i)
    lst4=lst3+lst2
print(lst4)"""

#Second largest element:

"""arr=[2, 3, 1, 4, 5]
def second(arr):
    largest=secondlargest=float('-inf')
    for num in arr:
        if num>largest:
            secondlargest=largest
            largest=num
        elif num>secondlargest and num!=largest:
            secondlargest=num
    return secondlargest
print(second(arr))"""

#Kth smallest:

"""arr=[12, 3, 5, 7, 19]
k = 2
def kth_smallest(arr,k):
    for i in range(k):
        smallest=float('inf')
        for num in arr:
            if num<smallest:
                smallest=num
        arr.remove(smallest)
    return smallest
print(kth_smallest(arr,k))"""

#kth largest

"""arr=[12, 3, 5, 7, 19]
k = 2
def kth_largest(arr,k):
    for i in range(k):
        largest=float('-inf')
        for num in arr:
            if num>largest:
                largest=num
        arr.remove(largest)
    return largest
print(kth_largest(arr,k))"""


#Missing sequence:

"""arr=[1, 2, 4, 5, 6]
def missing(arr):
    n=len(arr)+1
    res=0
    total=n*(n-1)//2
    actual=sum(arr)
    res=actual-total
    return res
print(missing(arr))"""

#Find the duplicates:
"""from collections import defaultdict
arr=[1, 2, 3, 4, 4, 5, 6, 7, 7]
def finddupl(arr):
    res=set()
    count=set()
    for num in arr:
        if num in count:
            res.add(num)
        else:
            count.add(num)
    return list(res)
print(finddupl(arr))"""

#isSorted:
"""arr=[1, 2, 3, 4, 5]
def isSorted(arr):
    for i in arr:
        if arr[i]<arr[i+1]:
            return True
    return False
print('arr is  Sorted: ',isSorted(arr))"""

#Largest Contigious Subarray sum:
"""arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
def subsum(arr):
    curr_sum=0
    max_sum=float('-inf')
    for num in arr:
        curr_sum=max(num,curr_sum+num)
        max_sum=max(max_sum,curr_sum)
    return max_sum
print(subsum(arr))"""

#Frequency of elements:
"""arr=[1, 2, 2, 3, 3, 3, 4]
def frequency(arr):
    freq={}
    for num in arr:
        freq[num]=freq.get(num,0)+1
    return freq
print(frequency(arr))"""

#Intersection of Two arr:
"""arr1=[1, 2, 2, 1]
arr2=[2, 2]
def intersection(arr1,arr2):
    res=[]
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]==arr2[j]:
                res.append(arr1[i])
                arr2[j]=None
                break
    return res
print(intersection(arr1,arr2))"""

#Power of Two
"""n=int(input("Enter:"))
def power(n):
    for i in range(n):
        if n>0 and n&(n-1)==0:
            return True
    return False
print(power(n))"""

# is a Palindrome
"""def ispalindrome(s):
    l,e=0,len(s)-1
    while l<e:
        if s[l]==s[e]:
            return True
        l+=1
        e-=1
    return False
s=str(input("Enter:"))
print(ispalindrome(s))"""

#Longest substring w/o repeating char:
"""s="abcabcbb"
def longest(s):
    res=set()
    max_len=0
    l=0
    for r in range(len(s)-1):
        while s[r] in res:
            res.remove(s[l])
            l+=1
        res.add(s[r])
        max_len=max(max_len,r-l+1)
    return max_len
print(longest(s))"""


#Reverse a str:
"""s="hello"
def reverse(s):
    res=''
    for i in s:
       res=i+res
    return res
print(reverse(s))"""

#BinarySearch:
"""arr=[1, 3, 5, 7, 9]
target = 5
def binary(arr,target):
    l,r=0,len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            l+=1
        else:
            r-=1
    return -1
print(binary(arr,target))"""

#find majority element:
"""arr=[3, 3, 4, 2, 4, 4, 2, 4, 4]
def majority(arr):
    res={}
    n=len(arr)
    for num in arr:
        res[num]=res.get(num,0)+1
        if res[num]>n//2:
            return num
    return None
print(majority(arr))"""

#left array rotation:
"""arr=[1, 2, 3, 4, 5, 6, 7]
k = 3
def leftrotation(arr,k):
    for i in range(k):
        temp=arr[0]
        for j in range(len(arr)-1):
            arr[j]=arr[j+1]
        arr[-1]=temp
    return arr
print(leftrotation(arr,k))"""

#Right array rotation:
"""arr=[1, 2, 3, 4, 5, 6, 7]
k = 3
def rightrotation(arr,k):
    for i in range(k):
        temp=arr[-1]
        for j in range(len(arr)-1,0,-1):
            arr[j]=arr[j-1]
        arr[0]=temp
    return arr
print(rightrotation(arr,k))"""

#common prefix:
"""s=["flower", "flow", "flight"]
def prefix(s):
    s.sort()
    res=''
    for i in range(len(s[0])):
        if s[0][i]==s[-1][i]:
            res+=s[0][i]
        else:
            break
    return res
print(prefix(s))"""

#balanced parenthesis:
"""s="()[]{}"
def param(s):
    d={'(':')','[':']','{':'}'}
    res=[]
    for i in s:
        if i in d:
            res.append(i)
        else:
            if not res or d[res.pop()]!=i:
                return False
    return not res
print(param(s))"""

#Union of 2arr:
"""arr1=[1, 2, 3, 4]
arr2= [3, 4, 5, 6]
res=arr1+arr2
print(res)"""

#Peak element:
"""arr=[1, 3, 20, 4, 1, 0]
def peak(arr):
    l,r=0,len(arr)-1
    while l<r:
        mid=(l+r)//2
        if arr[mid]>arr[mid+1]:
            r=mid
        else:
            l=mid+1
    return arr[l]
print(peak(arr))"""

#count ele:
"""arr=[1, 2, 2, 3, 2, 4, 5]
element = 2
count=0
for i in arr:
    if i==element:
        count+=1
print(count)"""

#Appear Once:
"""arr=[2, 2, 3, 3, 4, 5, 5]
def once(arr):
    unique=0
    for i in arr:
        unique ^=i
    return unique
print(once(arr))"""

#Longest Consequtive seq:
"""arr=[100, 4, 200, 1, 3, 2]
def seq(arr):
    longest=0
    res=set(arr)
    for i in arr:
        if i-1 not in res:
            length=1
        while i+ length in arr:
            length+=1
        longest=max(longest,length)
    return longest
print(seq(arr))"""

#Cummulative sum:
"""arr=[1,2,3,4]
def c_sum(arr):
    res=[]
    count=0
    for i in arr:
        count+=i
        res.append(count)
    return res
print(c_sum(arr))"""

#Positive cummulative sum:
"""arr=[1,-2,3,4,-6]
def p_sum(arr):
    res=[]
    plst=[]
    count=0
    for i in arr:
        count+=i
        res.append(count)
        if count>0:
            plst.append(count)
    return plst
print(p_sum(arr))"""

#Identical_Twins:
"""arr=[1,2,3,2,1]
def twins(arr):
    freq={}
    dupl=set()
    for num in arr:
        freq[num]=freq.get(num,0)+1
        if freq[num] >1:
            dupl.add(num)
    return len(dupl)
print(twins(arr))"""

#Even digit place
"""arr=[42, 564, 5775, 34, 123, 454, 1, 5, 45, 3556, 23442]
def even(arr):
    return[i for i in arr if(len(str(i))) %2==0]
print(even(arr))"""

#insertionsort
"""arr=[5 ,4, 2, 5, 3, 1]
def ins(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print(ins(arr))"""

#Merge Two Sorted Arrays
"""arr1= [1, 2, 3, 4, 4]
arr2=[2, 4, 5, 5]
def merge(arr1,arr2):
    res=[]
    s,e=0,0
    while s<len(arr1) and e<len(arr2):
        if arr1[s]<arr2[e]:
            res.append(arr1[s])
            s+=1
        else:
            res.append(arr2[e])
            e+=1
    while s<len(arr1):
        res.append(arr1[s])
        s+=1
    while e<len(arr2):
        res.append(arr2[e])
        e+=1
    return res
print(merge(arr1,arr2))"""

#Merge SortedSub array:
"""arr= [1, 3, 5, 7, 9, 11, 0, 4, 6, 8]
endindex=5
def mergesub(arr,endindex):
    i,j,k=0,0,0
    left=arr[:endindex+1]
    right=arr[endindex+1:]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
    return arr
print(mergesub(arr,endindex)) """


#Square sorted array:
"""arr=[6, -8, 3, -1, 4]
def square(arr):
    res=[i**2 for i in arr]
    return sorted(res) 
print(square(arr))"""

#maximum consecutive once:
"""arr=[1, 1, 3, 2, 3, 1, 1, 1]
def maxcon(arr):
    max_cn=0 #maximum count=0
    curr_cn=0 #current count=0
    for i in arr:  #itterate through
        if i==1:   #num=1
            curr_cn+=1 #current count add that 1. curr_cn=1
        else:
            curr_cn=0  # num is not 1 then curr_cn=0
        if curr_cn>max_cn:  #alaways curr_cn is grater.
            max_cn=curr_cn  
    return max_cn
print(maxcon(arr))"""


#longest increasing subsequence:
arr=[10, 22, 9, 33, 21, 50, 41, 60, 80]
def subseq(arr):
    n=len(arr)
    if not arr:
        return
    dp=[1]*n
    for i in range(1,n):
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)
print(subseq(arr))






        


        




        



        






            








