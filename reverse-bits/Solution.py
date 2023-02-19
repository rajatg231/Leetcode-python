// https://leetcode.com/problems/reverse-bits

class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for j in range(32):
            if n&1==0:
                res=2*res+0
            else:
                res=2*res+1
            n=n>>1
        return res