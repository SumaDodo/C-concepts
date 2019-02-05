class Solution:
    def addBinary(self, a: 'str', b: 'str') -> 'str':
        c, output = '0',''
        #padding with zeros
        a = '0'*(len(b)-len(a))+a if len(b)>len(a) else a
        b = '0'*(len(a)-len(b))+b if len(a)>len(b) else b
        
        #addition rules
        #if a+b is >1 then replace with zero and carry 1 else same
        for i in range(len(a)-1,-1,-1):
            total = (a[i]+b[i]+c).count('1')
            sum_ = '1' if total%2 else '0'
            c = '0' if total<2 else '1'
            output = sum_ + output
            
        return (c + output) if c == '1' else output
        
