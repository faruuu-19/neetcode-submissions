class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount={}
        tcount={}
        for alph in s:
            scount[alph]= 0
        for alph in s:
            scount[alph]= scount[alph]+1
        for alph in t:
            tcount[alph]= 0
        for alph in t:
            tcount[alph]= tcount[alph]+1
        for it in scount:
            if it in tcount:
                if tcount[it]!=scount[it]:
                    return False
            else:
                return False
        for it in tcount:
            if it in scount:
                if tcount[it]!=scount[it]:
                    return False
            else:
                return False
        return True