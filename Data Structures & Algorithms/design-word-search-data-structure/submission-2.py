class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(root, i):
            if i >= len(word) and root.endOfWord: 
                return True
            elif i >= len(word) or not root.children:
                return False

            # if I get a "." recurse on each children of that node
            # if a specific letter, recurse only on that letter
            if word[i] == ".":
                res = False
                for child in root.children:
                    if dfs(root.children[child], i + 1): res = True
                return res
            else:
                if word[i] not in root.children: return False

                res = False
                for child in root.children:
                    if child == word[i] and dfs(root.children[word[i]], i + 1):
                        res = True
                return res
        return dfs(self.root, 0)
        

