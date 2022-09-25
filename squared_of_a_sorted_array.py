class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            if nums[i] >= 0:
                break
                
        negs = nums[0:i]
        poss = nums[i:]
        
        negs.reverse()
        negs = [i**2 for i in negs]
        poss = [i**2 for i in poss]
        
        # concatenate two sorted arrays
        # using two pointers
        
        i = 0
        j = 0
        index = 0
        
        while i < len(negs) and j < len(poss):
            if i >= len(negs):
                nums[index] = poss[j]
                j += 1
            elif j >= len(poss):
                nums[index] = negs[i]
                i += 1
            elif negs[i] > poss[j]:
                nums[index] = poss[j]
                j += 1
            elif negs[i] < poss[j] or negs[i] == poss[j]:
                nums[index] = negs[i]
                i += 1
            index += 1
        return nums
                
        
        
        
            
        