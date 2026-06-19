class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        ans = 0
        n = len(nums)

        for i in range(n):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                length = 1

                for j in range(i + 1, n):
                    if nums[j] > threshold or nums[j] % 2 == nums[j - 1] % 2:
                        break
                    length += 1

                ans = max(ans, length)

        return ans
