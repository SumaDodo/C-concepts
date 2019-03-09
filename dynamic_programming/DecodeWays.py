class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        elif s[0] == "0":
            return 0
        
        dp = [0]*(len(s)+1)
        
        dp[len(s)] = 1
        dp[len(s)-1] = 1 if s[-1]!= "0" else 0
        
        for i in reversed(range(len(s)-1)):
            if s[i] == "0": continue
                
            dp[i] = dp[i+1]
            if int(s[i:i+2]) <= 26:
                dp[i] += dp[i+2]
                
        return dp[0] 
