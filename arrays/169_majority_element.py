class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        highest = 0
        majority = 0
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        for key, value in counter.items():
            if value > highest:
                majority = key
                highest = value
        return majority