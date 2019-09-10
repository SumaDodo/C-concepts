import collections

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_s = {}
        map_t = {}
        
        for i in range(len(s)):
            if s[i] in map_s:
                if map_s[s[i]] != t[i]:
                    return False
            elif t[i] in map_t:
                return False
            else:
                map_s[s[i]] = t[i]
                map_t[t[i]] = True
                
        return True
