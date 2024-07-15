class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, val in enumerate(nums):
            if val == target:
                return index
            if val > target:
                return index 
            if index == len(nums) -1 and val != target:
                return index + 1