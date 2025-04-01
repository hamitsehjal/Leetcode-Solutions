class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()

        for product in products:
            cur = root
            for ch in product:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]

                cur.suggestions.append(product)
                cur.suggestions.sort()
                if len(cur.suggestions) > 3:
                    cur.suggestions.pop()
        
        cur = root
        res = []

        for ch in searchWord:
            if ch in cur.children:
                cur = cur.children[ch]
                res.append(cur.suggestions)
            else:
                cur.children = {}
                res.append([])
        
        return res


            
        