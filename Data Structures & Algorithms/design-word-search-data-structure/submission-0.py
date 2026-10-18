class TrieNode:
    def __init__(self, char, children):
        self.char = char
        self.children = children
        self.endWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode(None, {})

    def addWord(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter in current.children:
                current = current.children[letter]
            else:
                current.children[letter] = TrieNode(letter, {})
                current = current.children[letter]
        current.endWord = True
        

    def search(self, word: str) -> bool:
        current = self.root
        def recursiveStep(current, word):
            for i in range(len(word)):
                if word[i] in current.children:
                    current = current.children[word[i]]
                elif word[i] == '.':
                    for key in current.children:
                        if recursiveStep(current.children[key], word[i + 1:len(word)]):
                            return True
                    return False
                else:
                    return False
            return current.endWord
        return recursiveStep(current, word)


        
