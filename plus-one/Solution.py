// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-1
        def add(digits,j):
            digits[j]+=1
            if(digits[j]>9):
                digits[j]%=10
                return 1
            else:
                return 0
        while(i>=0):
            if(i==len(digits)-1):
                car=add(digits,i)
                while(car==1)and(i>0):
                    car=add(digits,i-1)
                    i-=1
                else:
                    break
        if car==1:
            digits.insert(0,1)
        return digits