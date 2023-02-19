// https://leetcode.com/problems/counting-bits

class Solution:
    def countBits(self, n: int) -> List[int]:
        # res= [None]*(n+1)
        BitArr=[None]*(n+1)
        BitArr[0]=0
        def BitCount(num):
            count=0
            if(BitArr[num]==None):
                count+=BitCount(num & num-1)+1
            else:
                count+=BitArr[num]
            BitArr[num]=count
            return count
        for i in range(n+1):
            # res[i]=BitCount(i)
            BitCount(i)
        return BitArr
