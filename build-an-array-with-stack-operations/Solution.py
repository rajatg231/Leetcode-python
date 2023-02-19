// https://leetcode.com/problems/build-an-array-with-stack-operations

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        count=0
        for i in range(1,n+1):
            if(target[count]==i):
                res.append('Push')
                count+=1
            else:
                res.append('Push')
                res.append('Pop')
            if(count==len(target)):
                return res
        return res

        