class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        print("hi")
        b=0
        e=1
        maxlen=0
        while e<=len(s):
            print(s[b:e])
            if(len(s[b:e])==len("".join(set(s[b:e])))):
                maxlen=max(maxlen,len(s[b:e]))
            else:
                b+=1
            e+=1
        return maxlen

            

        