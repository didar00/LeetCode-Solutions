class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:   
        distances = list()
        
        for i in arr:
            distances.append(abs(i-x))

        # find the subarray of size k
        # with the smallest sum
        # use the sliding window technique
        
        i = 0
        min_ = 0
		
		# calculate the initial total distance
		# using the first window with size k
        for z in range(k):
            min_ += distances[i]
        
        temp = min_
        indices = [i, k-1]
        for j in range(k, len(distances)):
            temp = temp - distances[i] + distances[j]
            i += 1
            if temp < min_:
                indices = [i, j]
                min_ = temp

        return arr[indices[0]:indices[1]+1]