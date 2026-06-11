class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()

        count = 0

        for ch in s:

            if ch not in seen:

                seen.add(ch)

                count += 1

        return count
