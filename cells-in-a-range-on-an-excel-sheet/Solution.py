// https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res=[]
        charDiff=ord(s[3])-ord(s[0])+1
        numDiff=int(s[4])-int(s[1])+1
        for i in range(charDiff):
            for j in range(numDiff):
                res.append(chr(ord(s[0])+i)+
                str(int(s[1])+j))
        return res

