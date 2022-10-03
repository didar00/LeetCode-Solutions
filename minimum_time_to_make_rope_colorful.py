class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        consecutives = dict()
        
        i = 1
        prev = colors[0]
        count = 0
        while i < len(colors):
            if colors[i] == prev:
                if count not in consecutives:
                    consecutives[count] = [neededTime[i-1]]
                consecutives[count].append(neededTime[i])
            else:
                prev = colors[i]
                count +=1
            i+=1

        sum_ = 0
        for list_ in consecutives.values():
            if len(list_) == 1:
                sum_ += list_[0]
            else:
                max_ = 0
                for i in list_:
                    sum_+=i
                    max_ = max(max_, i)
                sum_ -= max_
        return sum_