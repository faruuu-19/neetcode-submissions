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
                if key == 'a':
                    freq[0] += hashmap[word][key]
                elif key == 'b':
                    freq[1] += hashmap[word][key]
                elif key == 'c':
                    freq[2] += hashmap[word][key]
                elif key == 'd':
                    freq[3] += hashmap[word][key]
                elif key == 'e':
                    freq[4] += hashmap[word][key]
                elif key == 'f':
                    freq[5] += hashmap[word][key]
                elif key == 'g':
                    freq[6] += hashmap[word][key]
                elif key == 'h':
                    freq[7] += hashmap[word][key]
                elif key == 'i':
                    freq[8] += hashmap[word][key]
                elif key == 'j':
                    freq[9] += hashmap[word][key]
                elif key == 'k':
                    freq[10] += hashmap[word][key]
                elif key == 'l':
                    freq[11] += hashmap[word][key]
                elif key == 'm':
                    freq[12] += hashmap[word][key]
                elif key == 'n':
                    freq[13] += hashmap[word][key]
                elif key == 'o':
                    freq[14] += hashmap[word][key]
                elif key == 'p':
                    freq[15] += hashmap[word][key]
                elif key == 'q':
                    freq[16] += hashmap[word][key]
                elif key == 'r':
                    freq[17] +=  hashmap[word][key]
                elif key == 's':
                    freq[18] +=  hashmap[word][key]
                elif key == 't':
                    freq[19] +=  hashmap[word][key]
                elif key == 'u':
                    freq[20] += hashmap[word][key]
                elif key == 'v':
                    freq[21] +=  hashmap[word][key]
                elif key == 'w':
                    freq[22] +=  hashmap[word][key]
                elif key == 'x':
                    freq[23] +=  hashmap[word][key]
                elif key == 'y':
                    freq[24] +=  hashmap[word][key]
                elif key == 'z':
                    freq[25] +=  hashmap[word][key]
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