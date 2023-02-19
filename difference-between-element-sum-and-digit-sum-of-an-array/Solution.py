// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def digiSum(number):
            sum=0
            while(number>0):
                sum+= number%10
                number= number//10
            return sum
        eleSum=0
        digitSum=0
        for num in nums:
            eleSum+=num
            if(num>9):
                digitSum+=digiSum(num)
            else:
                digitSum+=num
        return abs(eleSum-digitSum)
        