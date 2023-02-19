// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr=''.join(x for x in s if x.isalnum())
        newStr=newStr.upper()
        left=0
        right=len(newStr)-1
        while(left<=right):
            if(newStr[left]!=newStr[right]):
                return False
            else:
                left+=1
                right-=1
        return True