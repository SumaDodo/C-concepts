class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        i = 0
        while carry and i < len(digits):
            sum_val = digits[~i]+carry
            carry, digits[~i] = divmod(sum_val,10)
            i+=1
            
        if carry:
            return [carry]+digits
        else:
            return digits
