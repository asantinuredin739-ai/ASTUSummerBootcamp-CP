class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        total = 0

        for num in nums:
            total += num

        remainder = total % k
        return remainder
        
