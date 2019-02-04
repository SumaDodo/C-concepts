class TrieNode(object):
    """
    Learning Trie implementation in python
    1. each node stores char of the string
    2. children is a list of characters
    3. if the word is finished then mark it
    4. a counter to check how many times the character appeared in addition process
    """

    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1

def add_word(root, word: str):
    node = root
    for char in word:
        found_in_child = False
        #check if already present
        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child
                found_in_child = True
                break
        #If not add new child
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    node.word_finished = True

def find_prefix(root, prefix:str):
    """
    :param prefix: the prefix to be checked if present
    :return: counter, if present
    """
    node = root
    if not root.children:
        return False,0
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return False, 0

    return True, node.counter

if __name__ == "__main__":
    root = TrieNode('*')
    add_word(root, "hackathon")
    add_word(root, 'hack')

    print(find_prefix(root, 'hac'))
    print(find_prefix(root, 'hack'))
    print(find_prefix(root, 'hackathon'))
    print(find_prefix(root, 'ha'))
    print(find_prefix(root, 'hammer'))

