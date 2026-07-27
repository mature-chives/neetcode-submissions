class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        n = len(nums)
        dp = [[-1] * (target + 1) for _ in range(n + 1)]

        def dfs(i, target):
            if target == 0:
                return True
            if i >= n or target < 0:
                return False
            if dp[i][target] != -1:
                return dp[i][target]
            dp[i][target] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            return dp[i][target]
            
        
        return dfs(0, target)