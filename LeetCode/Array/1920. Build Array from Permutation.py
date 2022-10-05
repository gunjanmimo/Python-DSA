from typing import List
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        out_arr = []
        for i in range(len(nums)):
            out_arr.append(nums[nums[i]])
        return out_arr
        