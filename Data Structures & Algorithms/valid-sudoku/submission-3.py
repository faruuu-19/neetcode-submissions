class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i , row in enumerate(board):
            freq={}
            for num in row:
                if num in freq:
                    freq[num]+=1
                else:
                    freq[num]=1
                if freq[num]>1 and num!='.':
                    print("hi1")
                    return False
            print(freq)
        boardT=[]
        for i in range(len(board[0])):
            col = [row[i] for row in board]
            boardT.append(col)
        for i , row in enumerate(boardT):
            freq={}
            for num in row:
                if num in freq:
                    freq[num]+=1
                else:
                    freq[num]=1
                if freq[num]>1 and num!='.':
                    print("hi2")
                    return False
            print(freq)
        subgrids = {}
        k=0
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                temp = [row[j:j+3] for row in board[i:i+3]]
                subgrids[k]=temp
                k+=1
        for key in subgrids:
            flat=[]
            for subarr in subgrids[key]:
                flat.extend(subarr)
            while '.' in flat:
                flat.remove('.')
            flatset=set(flat)
            print(flat)
            if len(flatset)!= len (flat):
                print("hi3")
                return False

        return True



        