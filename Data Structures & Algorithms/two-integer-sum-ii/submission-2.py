class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        end=len(numbers)-1
        while start<end:
            print(start , end)
            while (numbers[start]+numbers[end]>target) and start<end:
                end-=1
                print("large" , start , end)
            if (numbers[start]+numbers[end]==target):
                break
            while(numbers[start]+numbers[end]<target) and start <end:
                start+=1
                print("small" , start , end)
            if (numbers[start]+numbers[end]==target):
                break
        print(start, end)
        return sorted([start+1 ,end+1])