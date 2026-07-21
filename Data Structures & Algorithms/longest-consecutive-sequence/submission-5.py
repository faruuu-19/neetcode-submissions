class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        numss=list(sorted(set(nums)))
        print(numss)
        maxconsec=1
        consec=1
        for i in range(len(numss)-1):
            print("diff", numss[i+1]-numss[i])
            if numss[i+1]-numss[i]==1 or numss[i+1]-numss[i]==-1:
                consec+=1
                if maxconsec<consec:
                    maxconsec=consec
            else:
                if maxconsec<consec:
                    maxconsec=consec
                consec=1
            print(consec , maxconsec)
        return maxconsec




        