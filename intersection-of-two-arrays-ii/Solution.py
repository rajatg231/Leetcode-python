// https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1.sort()
        # nums2.sort()
        # i=0
        # j=0
        # res=[]
        # while((i<len(nums1))and(j<len(nums2))):
        #     if(nums1[i]>nums2[j]):
        #         j+=1
        #     elif (nums1[i]<nums2[j]):
        #         i+=1
        #     else:
        #         res.append(nums1[i])
        #         i+=1
        #         j+=1              
        # return res
        res=[]
        d={}
        for i in nums1:
            if(d.get(i,-1)==-1):
                d[i]=1
            else:
                d[i]+=1
        for i in nums2:
            if(d.get(i,-1)>0):
                res.append(i)
                d[i]-=1
        return res
