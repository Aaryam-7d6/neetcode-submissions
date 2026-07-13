class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        n = len(nums)
        for x in range(n+1):
            if x not in s:
                return x