class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        string_list = list(s)
        char_list = []
        
        for i in range(len(s)):
            curr_char = string_list[i]
            if curr_char in char_list:
                char_list = char_list[char_list.index(curr_char)+1:len(char_list)]
            char_list.append(curr_char)
            if len(char_list)>length:
                length = len(char_list)
        return length 
