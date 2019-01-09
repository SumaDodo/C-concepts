class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        answer = []  
        
        def helper_function(rem,s_prev,idx):
            if rem=='': return
            if rem[0]=='0': 
                if idx<=2:
                    helper_function(rem[1:],s_prev+rem[:1]+'.',idx+1)
                elif len(rem)==1:
                    answer.append(s_prev+rem)
                return
            # ensure there are numbers and the numbers are all valid
            
            if idx<=2:
                if len(rem)>=1:
                    helper_function(rem[1:],s_prev+rem[:1]+'.',idx+1)
                if len(rem)>=2:
                    helper_function(rem[2:],s_prev+rem[:2]+'.',idx+1)
                if len(rem)>=3 and int(rem[:3])<=255:
                    helper_function(rem[3:],s_prev+rem[:3]+'.',idx+1)
                return
                
            if idx==3 and int(rem)<=255:
                answer.append(s_prev+rem)
                return
                
        helper_function(s,'',0)
        return answer
