// https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        dict={}
        dict['I']=1
        dict['V']=5
        dict['X']=10
        dict['L']=50
        dict['C']=100
        dict['D']=500
        dict['M']=1000
        set1= set(['IV','IX','XL','XC','CD','CM'])
        set
        def extra(str):
            if str=='IV':
                return 4
            if str=='IX':
                return 9
            if str=='XL':
                return 40
            if str=='XC':
                return 90
            if str=='CD':
                return 400
            if str=='CM':
                return 900
        res=0
        i=0
        while i<len(s):
            if((i<len(s)-1)and(s[i]+s[i+1]) in set1):
                res+=extra(s[i]+s[i+1])
                i+=2
            else:
                res+=dict[s[i]]
                i+=1
        return res
