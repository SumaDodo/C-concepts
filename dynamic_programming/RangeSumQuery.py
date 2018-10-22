class NumArray:

    def __init__(self, nums):
        """

        :param nums: List[int]
        """
        self.nums = nums
        self.rec = [0] * (len(nums)+1)
        self.maxind = -1

    def sumRange(self,i, j):
        """

        :param i: int
        :param j: int
        :return: int
        """
        sum1 = 0
        for z in range(self.maxind,j+1):
            self.rec[z+1] = self.rec[z] + self.nums[z]
        self.maxind = j
        print(self.rec[j+1] - self.rec[i])
