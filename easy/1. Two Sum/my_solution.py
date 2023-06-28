class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = []
        
        for i in range(len(nums) - 1):
            indices.append(i)
            
            for j in range(i + 1, len(nums)):
                
                if nums[j] + nums[indices[0]] == target:
                    indices.append(j)
                    return indices
                
            indices.clear()
                
        return indices