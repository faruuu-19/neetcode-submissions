class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        b=0
        e=1
        hm={}
        hm[s[b]]=1
        maxlen=1
        # print("maxlen: " , maxlen)
        # print(hm)
        while e<len(s):
            
            currlen=0
            # print("maxlen:" , maxlen , "b:" , b , "e: ", e)
            # print(hm)
            if s[e] in hm:
                # print("true for ", s[e])
                hm[s[e]]+=1
                while(hm[s[e]]>1):

                    
                    hm[s[b]]-=1
                    b+=1
                    # print("[s[b]",s[b])
                    # print("maxlen:" , maxlen , "b:" , b , "e: ", e)
                    # print(hm)
            else:
                hm[s[e]]=1
            currlen=e-b+1
            maxlen=max(maxlen , currlen)  
            # print("maxlen:" , maxlen , "b:" , b , "e: ", e)
            # print(hm)
            e+=1
            
        return maxlen


            

        