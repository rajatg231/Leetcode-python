// https://leetcode.com/problems/string-to-integer-atoi

class Solution:
    def myAtoi(self, s: str) -> int:
        num=0
        flag='pos'
        flagset=0
        set1=set(['0','1','2','3','4','5','6','7','8','9'])
        s=s.lstrip()
        # for c in s:
        i=0
        while i<len(s):
            c=s[i]
            if c=="+" or c=="-":
                if flagset==0 and i==0:
                    if c=="+":
                        flag='pos'
                    else:
                        flag='neg'
                    flagset=1
                    i+=1
                else:
                    break
            elif (c in set1):
                if num==0 and c=='0':
                    i+=1
                elif num==0:
                    num=int(c)
                    i+=1
                else:
                    num=num*10
                    num+=int(c)
                    i+=1
            else:
                break
        if flag=='neg':
            num=num*-1
        if (num> (2**31)-1):
            return (2**31)-1
        elif (num<-2**31):
            return -(2**31)
        else:
            return num
        
        
