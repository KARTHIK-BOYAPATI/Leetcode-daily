class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = max(set(nums),key=nums.count)
        return ans