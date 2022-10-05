class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out_arr = []
        for i in range(len(nums)):
            out_arr.append(sum(nums[:i+1]))
        return out_arr