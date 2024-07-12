class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_traversed = {}
        for index,num in enumerate(nums):
            diff = target - num
            if diff in nums_traversed:
                return nums_traversed[diff], index
            else:
                nums_traversed[num] = index
        return -1