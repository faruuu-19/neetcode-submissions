class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=[]
        for string in strs:
            length=len(string)
            temp=string
            temp=str(length)+'£'+temp
            ans.append(temp)
        flat=''
        for subarr in ans:
            flat+=subarr
        print(flat)
        return flat


    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        print("decoding strtas")
        for j in range(len(s)):
            if i not in range(len(s)):
                break
            print(s[i])
            idx=s.find("£", i)
            if idx==-1:
                break
            print("idx , " , idx)
            print(s[i:idx])
            
            num=int(s[i:idx])
            digits= idx-i
            print(num)
            temp=s[i+1+digits:i+num+1+digits]
            print(temp)
            ans.append(temp)
            i+=num+1+digits
        return ans