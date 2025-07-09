class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Cost us O(len(word)) - O(25)
        """
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]

        cur.is_end_of_word = True

    def search(self, word: str) -> bool:
        return self._dfs(0,self.root,word)

    def _dfs(self,start: int, root: TrieNode | None, word:str) -> bool:
        cur = root

        for i in range(start,len(word)):
            ch = word[i]
            if ch == ".":
                for value in cur.children.values():
                    if self._dfs(i+1,value,word):
                        return True
                return False
            else:
                if ch not in cur.children:
                    return False
                cur = cur.children[ch]

        return cur.is_end_of_word


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
