class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s1=[]
        for char in s:
            if 'a'<=char <='z'or '0'<=char<='9':
                s1.append(char) 
        s2=s1[::-1]
        if s1==s2:
            return True
        else:
            return False
        