#Armstrong number:
"""n=int(input("Enter:"))
temp=n
sum=0
length=len(str(n))
while temp>0:
    digit=temp%10
    sum+=digit**length
    temp//=10
if sum==n:
    print("Armstrong num")
else:
    print("Not an Armstring num")"""

#Find All Substrings:
"""str1="Bhanu"
n=len(str1)
def substr(str1,n):
    substr=[]
    for i in range(n):
        for j in range(i+1,n+1):
            substr.append(str1[i:j])
    return substr
print(substr(str1,n))"""

#mtd2:
"""s="abcabc"
def numberOf(s):
    s1={'a':0,'b':0,'c':0}
    i,count=0,0
    for j in range(len(s)):
        s1[s[j]]+=1
        while all(s1.values()):
            count+=len(s)-j
            s1[s[i]] -=1
            i+=1
    return count
print(numberOf(s))"""

#Remove duplicates:
"""def remove(n):
    d=[]
    for i in n:
        if i not in d:
            d.append(i)
    return d
n=[10,20,10,30,30,40]
print(remove(n))
"""

#mtd2
"""def removeDuplicates(nums):
    nums.sort()
    i=0
    for j in range(1,len(nums)):
        if nums[j]!=nums[i]:
            i+=1
            nums[i]=nums[j]
    return i+1
nums=[10,10,20,10,30,40,20]
length=removeDuplicates(nums)
print(nums[:length])"""

#Remove Duplicates Charaters from  a String:
"""s='Bhanuua'
def removedupl(s):
    nodupl=[]
    for char in s:
        if char not in nodupl:
            nodupl.append(char)
        st=''.join(nodupl)
    return st
print(removedupl(s))"""

#mtd2:
"""s='bcabc'
def duplChar(s):
    nodupl=[]
    seen=set()
    last_occ={char:i for i ,char in enumerate(s)}
    for i,char in enumerate(s):
        if char not in nodupl:
            while nodupl and char < nodupl[-1] and i<last_occ[nodupl[-1]]:
                seen.remove(nodupl.pop())
            nodupl.append(char)
            seen.add(char)
    return "".join(nodupl)
print(duplChar(s))
"""

#Rotate right:
"""nums=[1,2,3,4,5,6,7]
k=3
def rotate(nums,k):
    n=len(nums)
    k=k%n
    nums.reverse()
    nums[:k]=reversed(nums[:k])
    nums[k:]=reversed(nums[k:])
    return nums
print(rotate(nums,k))"""

#Roatate Left:
"""nums=[1,2,3,4,5,6,7]
k=3
def rotate(nums,k):
    n=len(nums)
    k=k%n
    nums[:k]=reversed(nums[:k])
    nums[k:]=reversed(nums[k:])
    nums.reverse()
    return nums
print(rotate(nums,k))"""

#Majority Ele 2:
"""nums = [1, 2, 3, 4, 3, 4, 2, 3]
def majority(nums):
    freq = {}
    res = []
    n = len(nums)
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    for num, count in freq.items():
        if count > n / 3:
            res.append(num)
    return res
print(majority(nums))"""

#Majority ele 1:
nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]
def ele(nums):
    freq = {}
    n = len(nums)
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > n // 2:
            return num  
    return "No Majority Element"
print(ele(nums))
