class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, j):
            if i == n:
                return 0
            if dp[i][j + 1] != -1:
                return dp[i][j + 1]

            res = dfs(i + 1, j) # exclude
            if j == -1 or nums[j] < nums[i]:
                res = max(res, 1 + dfs(i + 1, i)) # max(exclude, include), include = 1 + dfs(i + 1, i)
            dp[i][j + 1] = res
            return res

        return dfs(0, -1)
