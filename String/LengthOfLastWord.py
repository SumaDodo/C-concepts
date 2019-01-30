class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_list = s.split()
        if word_list:
            last_word = word_list.pop()
            return len(last_word)
        return 0
        
            
