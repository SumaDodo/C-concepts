class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j = 0
        while (j <= len(haystack)-len(needle)):
            if(haystack[j:j+len(needle)] == needle):
                return j
            j+=1
        return -1
