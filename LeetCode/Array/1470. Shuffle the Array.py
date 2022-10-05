class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out_arr  = []
        for i in range(n):
            out_arr.append(nums[i])
            out_arr.append(nums[i+n])
        return out_arr
        