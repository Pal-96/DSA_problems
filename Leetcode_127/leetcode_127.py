class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dq = deque()
        visited = set()
        l = len(beginWord)
        visited.add(beginWord)
        dq.append([beginWord, 1])
        letters = set(string.ascii_lowercase)
        wl = set(wordList)
        if endWord not in wl:
            return 0
            
        while dq:
            beginWord, seq_no = dq.popleft()
            if beginWord == endWord:
                return seq_no
            for i in range(0, l):
                for c in letters:
                    if beginWord[i] == c:
                        continue
                    new_word = beginWord[:i] + c + beginWord[i+1:]
                    if new_word in wl and new_word not in visited:
                        dq.append([new_word, seq_no + 1])
                        visited.add(new_word)
        return 0