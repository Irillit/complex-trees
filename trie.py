class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word_end = False


class Trie:

    def __init__(self):
        self._root = TrieNode()

    def insert(self, word):
        curr = self._root

        for i, char in enumerate(word):
            idx = ord(char) - ord('a')

            if not curr.children[idx]:
                node = TrieNode()
                curr.children[idx] = node
                if i == len(word) - 1:
                    node.word_end = True
                curr = node
            else:
                curr = curr.children[idx]
                if i == len(word) - 1:
                    curr.word_end = True

    def search(self, word) -> bool:
        curr = self._root

        for i, char in enumerate(word):
            idx = ord(char) - ord('a')

            if not curr.children[idx]:
                return False

            curr = curr.children[idx]
            if i == len(word) - 1 and curr.word_end:
                return True

        return False

    def starts_with(self, prefix) -> bool:
        curr = self._root

        for char in prefix:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]

        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("add")
    trie.insert("address")
    trie.insert("look")
    trie.insert("book")

    print(trie.search("book"))
    print(trie.search("soup"))
    print(trie.search("addr"))
    print(trie.starts_with("addr"))
