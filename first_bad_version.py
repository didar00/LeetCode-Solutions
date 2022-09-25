# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        
        def search(low, high):
            if low > high:
                return low
            
            mid = (high + low)//2
            
            if isBadVersion(mid):
                return search(low, mid-1)
            else:
                return search(mid+1, high)
                    
            return low
        
        return search(1, n+1)