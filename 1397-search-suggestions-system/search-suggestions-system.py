class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Solution:
    def _find_prefix_node(self, prefix):
        cur = self.root

        for ch in prefix:
            if ch not in cur.children:
                return None
            cur = cur.children[ch]

        return cur

    def _dfs_prefix_node(self, node, current_prefix, results):
        if node.word:
            results.append(current_prefix)
        for ch, child_node in node.children.items():
            self._dfs_prefix_node(child_node, current_prefix + ch, results)

    def _getAllWordsWithPrefix(self, prefix):
        results = []
        prefix_node = self._find_prefix_node(prefix)

        if prefix_node:
            self._dfs_prefix_node(prefix_node, prefix, results)

        return results

    def autocomplete(self, prefix, maxSuggestions=3):
        all_words = self._getAllWordsWithPrefix(prefix)
        all_words.sort()
        return all_words[:3]

    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        self.root = TrieNode()

        for product in products:
            cur = self.root
            for ch in product:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]

            cur.word = True

        res = []

        for i in range(len(searchWord)):
            prefix = searchWord[:i+1]
            res.append(self.autocomplete(prefix))

        return res
