class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        length = len(board)
        def convertToindex(pos):
            r = (pos - 1)//length
            c = (pos - 1) % length
            if r%2:
                c = length - c - 1
            return [r,c]

        pq = deque() ## item can be removed from front and rear.
        visited = set() ## no duplicates, unordered, existence check O(1).
        pq.append([1,0])
        while pq:
            pos, moves = pq.popleft()
            for i in range(1,7):
                nextpos = pos + i
                r,c = convertToindex(nextpos)
                if board[r][c]!=-1:
                    nextpos = board[r][c]
                if nextpos == length*length:
                    return moves+1
                if nextpos not in visited:
                    visited.add(nextpos)
                    pq.append([nextpos, moves+1])
        return -1