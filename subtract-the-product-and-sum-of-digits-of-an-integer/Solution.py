// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1
        addition=0
        while(n>0):
            digit = n%10
            prod*=digit
            addition+=digit
            n=n//10
        return prod-addition