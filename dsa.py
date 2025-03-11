#Reverse a String
"""def reverse_str(str):
    reverse_str=" "
    for char in str: 
        reverse_str=char + reverse_str
    return reverse_str
str=input("enter from user : ")
res=reverse_str(str)
print(res)"""

#Find the Maximum Subarray Sum (Kadane's Algorithm)
def max_subarr_sum(arr):
    max_sum=float('-inf') 
    curr_sum=0
    for num in arr: 
        curr_sum=max(num,curr_sum+num)
        max_sum=max(max_sum,curr_sum)
    return max_sum 
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
res=max_subarr_sum(arr)
print(f'The max_subarr_sum  is: ',res)

