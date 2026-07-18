class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]].append(i)
            else:
                hashmap[nums[i]] = [i]

        for i in range(len(nums)):
            if (target - nums[i]) in hashmap:
                if i != min(hashmap[target - nums[i]]):
                    return sorted([i, min(hashmap[target - nums[i]])])