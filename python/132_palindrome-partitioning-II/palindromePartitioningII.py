class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [i-1 for i in range(n + 1)]
        for i in range(1, n+1):
            for j in range(i):
                temp = s[j:i]
                if temp == temp[::-1]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n]

mytest = Solution()
s = 'aab'
print mytest.minCut(s)
