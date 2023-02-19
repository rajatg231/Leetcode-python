// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=[0]*len(prices)
        max1=[0]*len(prices)
        # glomin=0
        min[0]=(prices[0])
        max1[len(prices)-1] = prices[len(prices)-1]
        for i in range(1,len(prices)):
            if min[i-1]>prices[i]:
                min[i]=prices[i]
            # if min[glomin]>prices[i]:
            #     glomin=i
            else:
                min[i]=min[i-1]
        for j in range(len(prices)-1,0,-1):
            if prices[j-1]>max1[j]:
                max1[j-1]=prices[j-1]
            else:
                max1[j-1]=max1[j]
        ans=0
        for i in range(len(min)):
            ans=max(ans,max1[i]-min[i])
        return ans

        
        
        # res=0
        # temp=prices[0]
        # for i in range(len(prices)-1):
        #     if prices[i+1]>temp:
        #         res+=prices[i+1]-temp
        #         temp=prices[i+1]
        #     elif temp==prices[0] and temp>prices[i]:
        #         temp=prices[i]
        # return res