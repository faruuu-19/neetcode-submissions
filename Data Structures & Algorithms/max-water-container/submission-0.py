class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=0
        s=0
        e=len(heights)-1
        while s<e:
            temp=min(heights[s],heights[e]) * (e-s)
            print(ans, temp)
            ans=max(ans , temp)
            if(heights[s]<heights[e]):
                s+=1
            else:
                e-=1
        
        return ans
            