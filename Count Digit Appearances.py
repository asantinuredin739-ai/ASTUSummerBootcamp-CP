class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        count=0
        for num in nums:
            if num ==0 and digit ==0:
                count+=1
                continue
            n=abs(num)
            while n>0:
                if n%10==digit:
                    count+=1
                n//=10
        return count
