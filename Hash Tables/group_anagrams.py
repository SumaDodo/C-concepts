import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_count = collections.defaultdict(list)
        for i in strs:
            anagram_count[tuple(sorted(i))].append(i)
            
        return anagram_count.values()
