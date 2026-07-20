class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h1={}
        answer=[]
        for num in nums:
            if num in h1:
                h1[num]+=1
            else:
                h1[num]=1
        print(h1)
        h2={}
        for key in h1:
            if h1[key] not in h2:
                h2[h1[key]]=[key]
            else:
                h2[h1[key]].append(key)
        print("ferf")
        print(h2)
        freq=sorted(list(h2.keys()))
        freq.reverse()
        ans=[]
        for f in freq:
            ans.append(h2[f])
        result = []
        for sublist in ans:
            result.extend(sublist)
        return result[:k]

        