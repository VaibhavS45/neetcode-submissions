class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        start,maxlen=0,0
        for end,char in enumerate(s):
            if char in seen and seen[char]>=start:
                start=seen[char]+1
            seen[char]=end
            curlen=end - start+1    
            if curlen > maxlen:
                maxlen=curlen
        return maxlen             