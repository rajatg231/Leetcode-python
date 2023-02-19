// https://leetcode.com/problems/count-primes

import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        flag=[1]*(n)
        flag[0]=0
        flag[1]=0
        # count=0
        N=math.floor(math.sqrt(n))
        for i in range(2,N+1):
        #     if flag[i]==True:
        #         count+=1
            # for j in range(2*i,n,i):
            #     flag[j]=0
            flag[i*i:n:i]=[0]*(((n-1-(i*i))//i)+1)
        count=0
        for f in flag:
            if f == 1:
                count+=1
        return count
        
            
