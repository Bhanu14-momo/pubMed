#permutation problem using backtracking
N=3
def permutation(N):
    res=[0]*(2*N) #array to store the final result
    def backtrack(num): #number down to 1
        if num ==0:   #if all numbers are placed
            return True
        for i in range(2*N-num-1):#place num in valid position
            if res[i] ==0 and res[i+num+1]==0: #+ve or empty
                res[i],res[i+num+1]=num,num #place number
                if backtrack(num-1): #recur for next numver
                    return True
                res[i],res[i+num+1]=0,0
        return False 
    return res if backtrack(N) else []
print(permutation(N))