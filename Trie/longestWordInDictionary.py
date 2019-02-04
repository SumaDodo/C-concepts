from functools import reduce
class Solution(object):
    def longestWord(self, words):
        words.sort()
        word_set, longest_word = set(['']),""
        for word in words:
            if word[:-1] in word_set:
                word_set.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
                    
        return longest_word
