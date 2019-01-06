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
        sum1 = collections.Counter(a+b for a in A for b in B)
        return sum(sum1[-c-d] for c in C for d in D)
