class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)

        res = []

        for n in nums2:
            if n in seen:
                seen.remove(n)
                res.append(n)
        return res