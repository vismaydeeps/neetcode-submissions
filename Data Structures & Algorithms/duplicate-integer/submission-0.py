class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n_set = set(nums)
        if len(n_set) == len(nums):
            return False
        return True