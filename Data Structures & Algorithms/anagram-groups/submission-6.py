class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        dup={}
        for string in strs:
            dup[string]=0
        for string in strs:
            hashmapi={}
            for char in string:
                if char in hashmapi:
                    hashmapi[char]+=1
                else:
                    hashmapi[char]=1
            if string in hashmap:
                dup[string]+=1
            hashmap[string]=hashmapi
        print(hashmap)
        print("efnkjewbf")
        print(dup)
        freqhashmap={}
        for word in hashmap:
            freq = [0] * 26
            for key in hashmap[word]:
               freq[ord(key) - ord('a')] += hashmap[word][key]
            freqtuple=tuple(freq)
            freqhashmap[word]=freqtuple
        print(freqhashmap)
        h2={}
        for key in freqhashmap:
            if freqhashmap[key] in h2:
                h2[freqhashmap[key]].append(key)
                for limit in range(dup[key]):
                    h2[freqhashmap[key]].append(key)
            else:
                h2[freqhashmap[key]] = [key]
                for limit in range(dup[key]):
                    h2[freqhashmap[key]].append(key)
        print("---------hjbv-------")
        print(h2)
        answer=[]
        for key in h2:
            answer.append(h2[key])


                
        return answer