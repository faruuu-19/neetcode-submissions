class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numss = sorted(nums)
        ans = []

        for t, target in enumerate(numss):
            s = 0
            e = len(numss) - 1

            while s < e:

                # Skip the target index
                if s == t:
                    s += 1
                    continue
                if e == t:
                    e -= 1
                    continue

                if numss[s] + numss[e] < -target:
                    s += 1

                elif numss[s] + numss[e] > -target:
                    e -= 1

                else:
                    triplet = sorted([numss[s], numss[e], target])
                    if triplet not in ans:
                        ans.append(triplet)
                    s += 1
                    e -= 1

        return ans