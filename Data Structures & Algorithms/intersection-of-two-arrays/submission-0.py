class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1set = set(nums1)
        nums2set = set(nums2)

        intersection = nums1set & nums2set

        ints = list(intersection)

        return ints