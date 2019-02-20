class Solution:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        len_s = len(s)
        len_t = len(t)
        
        if len_s != len_t:
            return False
        
        string_s = sorted(s)
        string_t = sorted(t)
        
        if string_s == string_t:
            return True
        else:
            return False
