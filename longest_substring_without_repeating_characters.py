class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window fashion
        i = 0
        max_ = 0
        index = 0
        temp = ""
        
        while index < len(s):
            if s[index] in temp:
                i = i + temp.find(s[index]) + 1
                temp = temp[temp.find(s[index])+1:]
            temp += s[index]
            index +=1
            max_ = max(max_, index-i)
        return max_