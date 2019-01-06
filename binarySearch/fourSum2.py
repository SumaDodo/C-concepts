import collections
class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        count = 0
        dictionary = {}
        for i in A:
            for j in B:
                val = i+j
                if val in dictionary:
                    dictionary[val]+=1
                else:
                    dictionary[val] = 1
                    
        for i in range(len(C)):
            for j in range(len(D)):
                target = 0 - (C[i]+D[j])
                if target in dictionary:
                    count += dictionary[target]
        return count
