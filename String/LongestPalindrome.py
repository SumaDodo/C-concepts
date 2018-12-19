class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i in range(len(s)):
            temp_result = self. helper_func(s, i, i)
            if(len(temp_result) > len(result)):
                result = temp_result
            temp_result = self.helper_func(s,i,i+1)
            if(len(temp_result) > len(result)):
                result = temp_result
        return result
            
    def helper_func(self, s, l, r):
        while (l>=0 and r<len(s) and s[l]==s[r]):
            l -=1
            r +=1
        return s[l+1:r]
