# Find the Sum of the Diagonal Elements of a Matrix

a=[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
n=3
prinmary_digonal,secondary_digonal=0,0
for i in range(len(a)): 
    for j in range(len(a[i])): 
        if i==j: 
            prinmary_digonal+=a[i][j]
        if i+j==(n-1): 
            secondary_digonal+=a[i][j]
if n%2==1:   #odd size matrix.
    mid=a[n//2][n//2]
    total_sum=prinmary_digonal+secondary_digonal-mid
else: 
    total_sum=prinmary_digonal+secondary_digonal
print(total_sum)

