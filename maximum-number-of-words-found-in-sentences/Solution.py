// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        out=0
        for i in range(len(sentences)):
            temp=sentences[i].count(" ")
            if(temp>=out):
                out=temp
        return out+1