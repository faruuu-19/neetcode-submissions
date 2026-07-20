class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:            
        freqhashmap={}
        h2={}
        for word in strs:
            freq = [0] * 26
            for key in word:
               freq[ord(key) - ord('a')] += 1
            freqtuple=tuple(freq)
            if freqtuple in h2:
                h2[freqtuple].append(word)
            else:
                h2[freqtuple] = [word]
        
    
        answer=[]
        for key in h2:
            answer.append(h2[key])


                
        return answer