class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()       
        pointer1=0           
        pointer2=0     
        count=0                 
        while pointer1<=len(g)-1  and pointer2<=len(s)-1:
            if g[pointer1]<=s[pointer2]:
                count+=1
                pointer1+=1
                pointer2+=1
            else:
                pointer2+=1
        return count
