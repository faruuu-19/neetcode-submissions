class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup={}
        for num in nums:
            if num in lookup:
                lookup[num]= lookup[num] + 1
            else:
                 lookup[num]= 1
        print(lookup)
        for key in lookup:
            if lookup[key]>1:
                return True
        return False
        



        