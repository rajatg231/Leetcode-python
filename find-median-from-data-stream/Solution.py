// https://leetcode.com/problems/find-median-from-data-stream

import heapq
class MedianFinder:

    def __init__(self):
        self.max=[]
        self.min=[]
        # heapq.heapify(self.min)
        # heapq._heapify_max(self.max)

    def addNum(self, num: int) -> None:
        if len(self.max)==len(self.min):
            heappush(self.max, -num) #for max heap make numbers negative, push in the max heap
            temp= heappop(self.max) #get the max number from max heap
            heappush(self.min , -temp)  #put in the min heap, because size of min heap will be kept bigger
        else:
            heappush(self.min, num) #push in the min heap
            temp= heappop(self.min) #get the min number from min heap 
            heappush(self.max , -temp)  #put in the max heap, because size of min heap will be kept bigger
        # if len(self.max)==len(self.min):
        #     heappush(self.min, -(heappushpop(self.max, -(num))))  #for max heap make numbers negative
        # else:
        #     heappush(self.max, -(heappushpop(self.min, (num))))  #for max heap make numbers negative
        # if len(self.max)==0 or num<=self.max[0] and len(self.min)>0:
        #     self.max.append(num)
        #     heapq._heapify_max(self.max)
        # elif len(self.min)==0 and num<=self.max[0]:
        #     temp=heapq._heappop_max(self.max)
        #     heapq.heappush(self.min, temp)
        #     self.max.append(num)
        #     heapq._heapify_max(self.max)       
        # else:
        #     heapq.heappush(self.min,num)
        # if(len(self.min)>0) and (len(self.max)>len(self.min)+1):
        #     temp=heapq._heappop_max(self.max)
        #     heapq.heappush(self.min,temp)
        # elif(len(self.max)>0) and (len(self.min)> len(self.max)):
        #     temp=heapq.heappop(self.min)
        #     self.max.append(temp)
        #     heapq._heapify_max(self.max)
        # if len(self.maxArr)>len(self.minArr) :
        #     if (len(self.maxArr)>0) and (len(self.minArr)>0) and num>self.maxArr[0] and num<=self.minArr[0]:
        #         heapq.heappush(self.minArr,num)
        #     elif (len(self.maxArr)>0) and (len(self.minArr)>0) and num<=self.maxArr[0]:
        #         heapq.heappush(self.minArr, heapq._heapreplace_max(self.maxArr, num))
        #     else:
        #         if self.maxArr[0]>num:
        #             heapq.heappush(self.minArr, heapq._heappop_max(self.maxArr))
        #             self.maxArr.append(num)
        #             heapq._heapify_max(self.maxArr)
        #         else:
        #             heapq.heappush(self.minArr,num)
        # elif len(self.maxArr)<len(self.minArr) :
        #     if (len(self.maxArr)>0) and (len(self.minArr)>0) and num>self.minArr[0]:
        #         temp=heapq.heappop(self.minArr)
        #         heapq.heappush(self.minArr,num)
        #         # self.maxArr.append(temp)
        #         # heapq._heapify_max(self.maxArr)
        #         self.maxArr.insert(0,temp)
        #     elif (len(self.maxArr)>0) and (len(self.minArr)>0) and num>self.maxArr[0] and num<=self.minArr[0]:
        #         self.maxArr.insert(0,num)
        #     else:
        #         if self.minArr[0]<num:
        #             temp=heapq.heappop(self.minArr)
        #             heapq.heappush(self.minArr,num)
        #             self.maxArr.append(temp)
        #             heapq._heapify_max(self.maxArr)
        #         else:
        #             self.maxArr.append(num)
        #             heapq._heapify_max(self.maxArr)
        # else:
        #     if(len(self.maxArr)==0):
        #         self.maxArr.append(num)
        #     elif(len(self.minArr)==0):
        #         heapq.heappush(self.minArr,num)
        #     elif num>=self.minArr[0]:
        #         heapq.heappush(self.minArr,num)
        #     elif num>=self.maxArr[0] and num<self.minArr[0]:
        #         self.maxArr.insert(0,num)
        #     else:
        #         self.maxArr.append(num)
        #         heapq._heapify_max(self.maxArr)

    def findMedian(self) -> float:
        if(len(self.max)==len(self.min)):
            return (self.min[0] - self.max[0])/2
        else:
            return self.min[0]
        # if(len(self.max)==len(self.min)):
        #     return (self.min[0] + self.max[0])/2
        # else:
        #     return self.max[0]
        
        # if(len(self.maxArr)>len(self.minArr)):
        #     # return heapq._heappop_max(self.maxArr)
        #     return self.maxArr[0]
        # elif len(self.maxArr)<len(self.minArr):
        #     # return heapq.heappop(self.minArr)
        #     return self.minArr[0]
        # else:
        #     return (self.minArr[0] + self.maxArr[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()