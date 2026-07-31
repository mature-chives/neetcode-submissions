class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = curMax = curMin = nums[0]
        
        for i in range(1, len(nums)):
            tmp = nums[i] * curMax
            curMax = max(nums[i], tmp, nums[i] * curMin)
            curMin = min(nums[i], tmp, nums[i] * curMin)
            res = max(res, curMax)

        return res