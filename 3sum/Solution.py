// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        i,j,k=0,0,0
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                target=nums[i]+nums[j]+nums[k]
                # if target==0:
                #     res.append([nums[i],nums[j],nums[k]])
                #     j+=1
                if target>0:
                    k-=1
                elif target<0:
                    j+=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                # target=nums[i]+nums[j]+nums[k]
                    while nums[j-1]==nums[j] and j<k:
                        j+=1
        return res
        # dict1={}
        # dict2={}
        # res=[]
        # # nums=list(set(nums))
        # for num in nums:
        #     if dict1.get(num,-1)==-1:
        #         dict1[num]=1
        #     else:
        #         dict1[num]+=1
        # nums=[]
        # for key in dict1:
        #     if dict1[key]>3:
        #         tr=4
        #     else:
        #         tr=dict1[key]
        #     for i in range(tr):
        #         nums.append(key) 
        # dict1={}
        # for num in nums:
        #     if dict1.get(num,-1)==-1:
        #         dict1[num]=1
        #     else:
        #         dict1[num]+=1     
        # def add(num,numi,numj,dict2):
        #     temp=[num,numi,numj]
        #     temp.sort()
        #     if (dict2.get(temp[0],'a')=='a'):
        #         dict2[temp[0]]=[temp]                 
        #     elif temp in dict2[temp[0]]:
        #         return
        #     else:
        #         dict2[temp[0]].append(temp)

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         target=0-nums[i]
        #         if i==j:
        #             continue
        #         else:
        #             tem=target-nums[j]
        #             if dict1.get(tem, -1)!=-1:    
        #                 if nums[i]==tem and nums[j]==tem:
        #                     if dict1.get(tem, -1)>2:
        #                         add(nums[i],nums[j],tem,dict2)
        #                     continue  
        #                 elif nums[i]==tem or nums[j]==tem:
        #                     if dict1.get(tem, -1)>1:
        #                         add(nums[i],nums[j],tem,dict2)           
        #                 elif nums[i]!=tem:                            
        #                         add(nums[i],nums[j],tem,dict2)
        # for key in dict2:
        #     for val in dict2[key]:
        #         res.append(val)
        # return res

            