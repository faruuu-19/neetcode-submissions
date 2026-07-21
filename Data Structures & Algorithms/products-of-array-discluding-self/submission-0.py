class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pdt=1
        zero_tracker=0
        for i,num in enumerate(nums):
            pdt*=num
            if num==0:
                zero_tracker+=1
            else:
                zero_tracker==0
        idx=0
        if zero_tracker==1:
            idx= nums.index(0)
        pdtw0=1
        for i, num in enumerate(nums):
            if i!=idx:
                pdtw0*=num


        ans=[pdt]*len(nums)
        print(ans)
        print("zero_tracker" , zero_tracker)
        for i,a in enumerate(ans):
            if nums[i]!=0:
                ans[i]/=nums[i]
            else:
                if zero_tracker==1:
                    print("hi" , pdtw0)
                    ans[i]=pdtw0
                else:
                    ans[i]=0


            ans[i]=int(ans[i])
        return ans
        