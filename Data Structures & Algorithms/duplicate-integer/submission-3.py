class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup={}
        for i in range(len(nums)):
            if nums[i] in lookup:
                lookup[nums[i]]= lookup[nums[i]] + 1
            else:
                 lookup[nums[i]]= 1
        print(lookup)
        for key in lookup:
            if lookup[key]>1:
                return True
        return False
        



        