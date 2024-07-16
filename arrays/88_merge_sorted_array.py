class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m-1
        j = n-1
        replace_pos = len(nums1) - 1
        while replace_pos > -1:
            if i < 0 and j >= 0:
                nums1[replace_pos] = nums2[j]
                j-=1
                replace_pos-=1
            elif j < 0 and i>=0:
                nums1[replace_pos] = nums1[i]
                i-=1
                replace_pos-=1
            elif nums1[i] >= nums2[j]:
                nums1[replace_pos] = nums1[i]
                replace_pos -= 1
                i-=1
            else:
                nums1[replace_pos] = nums2[j]
                replace_pos -= 1
                j-=1
        return nums1