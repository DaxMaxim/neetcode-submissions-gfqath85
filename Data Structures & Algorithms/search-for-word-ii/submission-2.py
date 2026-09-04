class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        visit, res = set(), []

        # create a trie and add all words there.
        root = TrieNode()

        for word in words:
            cur = root

            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.endOfWord = True

        # loop on all the elements in the root's hashmap and do dfs
        def dfs(t_node, r, c, cur_path):
            
            visit.add((r, c))
            cur_path.append(board[r][c])

            if t_node.endOfWord:
                t_node.endOfWord = False
                res.append("".join(cur_path))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for chld in t_node.children:
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (0 <= row < ROWS and 0 <= col < COLS and
                        board[row][col] == chld and (row, col) not in visit):
                        dfs(t_node.children[chld], row, col, cur_path)
            visit.remove((r, c))
            cur_path.pop()

        for child in root.children:
            for r in range(ROWS):
                for c in range(COLS):
                    if board[r][c] == child: dfs(root.children[child], r, c, [])
        return res



