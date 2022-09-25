class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        j = 0
        # i is the end of the non zero list
        # j is the runner
        if len(nums) < 2:
            return
        
        
        while j < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                nums[i] = nums[j]
                nums[j] = 0
                i += 1 
            if nums[i] != 0:
                i += 1
            j+=1