class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word = False
    
    def __repr__(self):
        return f"{self.children.keys()}"

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()  

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        stack = [(0, curr)]
        while stack:
            char_idx, curr = stack.pop()
            if char_idx >= len(word):
                if curr.word:
                    return True
                else:
                    continue
            char = word[char_idx]
            if char == ".":
                for c, node in curr.children.items():
                    stack.append((char_idx + 1, node))
                continue
            if char in curr.children:
                stack.append((char_idx + 1, curr.children[char]))

        return False
