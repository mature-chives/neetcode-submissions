class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # top-down 
        # n = len(nums)
        # dp = [[-1] * (n + 1) for _ in range(n)]

        # def dfs(i, j):
        #     if i == n:
        #         return 0
        #     if dp[i][j + 1] != -1:
        #         return dp[i][j + 1]

        #     res = dfs(i + 1, j) # exclude
        #     if j == -1 or nums[j] < nums[i]:
        #         res = max(res, 1 + dfs(i + 1, i)) # max(exclude, include), include = 1 + dfs(i + 1, i)
        #     dp[i][j + 1] = res
        #     return res

        # return dfs(0, -1)

        # bottom-up dp[i][j]
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):# i in n-1...0
            for j in range(i - 1, -2, -1):# j in i-1...-1
                res = dp[i + 1][j + 1]
                if j == -1 or nums[j] < nums[i]:
                    res = max(res, 1 + dp[i + 1][i + 1])
                dp[i][j + 1] = res
        return dp[0][0]


