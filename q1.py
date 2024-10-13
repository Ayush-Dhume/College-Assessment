class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self.dfs(node, prefix)

    def dfs(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            words.extend(self.dfs(child_node, prefix + char))
        return words


def suggest_completions(search_history, partial_query):
    trie = Trie()
    for query in search_history:
        trie.insert(query)
    return trie.search(partial_query)


search_history = [
    "apple",
    "banana",
    "carrot",
    "pear",
    "pineapple",
    "potato",
    "strawberry"
]

partial_query = input("Enter your partial search query: ")
suggestions = suggest_completions(search_history, partial_query)

print("Suggestions:")
for suggestion in suggestions:
    print(suggestion)