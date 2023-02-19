// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for s in strs:
            temp=''.join(sorted(s))
            if dict.get(temp,-1)==-1:
                dict[temp]=[s]
            else:
                dict[temp].append(s)
        # res=[]
        # for key in dict:
        #     res.append(dict[key])
        return dict.values()

        # dict={'a':1 ,'b':2, 'c':3 , 'd':4 , 'e':5 , 'f':6 , 'g':7, 'h':8,
        # 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19,
        # 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
        # dct2={}
        # for s in strs:
        #     sum=0
        #     sum1=0
        #     ordsum=0
        #     for c in s:
        #         sum1+=(dict[c]*ord(c))
        #         ordsum+=ord(c)
        #     sum= sum1*ordsum
        #     sum=sum*len(s)
        #     if dct2.get(sum,-1)==-1:
        #         dct2[int(sum)]=[s]
        #     else:
        #         dct2[int(sum)].append(s)
        # res=[]
        # for key in dct2:
        #     res.append(dct2[key])
        # return res