class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)

        for ind, value in enumerate(nums):
            difference = target - value

            if difference in dic:
                return [dic[difference], ind]
            dic[value] = ind
