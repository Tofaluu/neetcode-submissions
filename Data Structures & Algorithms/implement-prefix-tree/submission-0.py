class TrieNode:
    def __init__(self, char, children):
        self.char = char
        self.children = children
        self.lastLetter = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode(None, {})

    def insert(self, word: str) -> None:
        currentTrie = self.root
        for letter in word:
            if letter in currentTrie.children:
                currentTrie = currentTrie.children[letter]
            else:
                currentTrie.children[letter] = TrieNode(letter, {})
                currentTrie = currentTrie.children[letter]
        currentTrie.lastLetter = True



    def search(self, word: str) -> bool:
        currentTrie = self.root
        for letter in word:
            if letter in currentTrie.children:
                currentTrie = currentTrie.children[letter]
            else:
                return False
        return currentTrie.lastLetter

    def startsWith(self, prefix: str) -> bool:
        currentTrie = self.root
        for letter in prefix:
            if letter in currentTrie.children:
                currentTrie = currentTrie.children[letter]
            else:
                return False
        return True

        