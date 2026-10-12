from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # Count character frequencies for both strings
        count_s = Counter(s)
        count_t = Counter(t)
        
        # The number of steps needed is the sum of differences where count_s > count_t
        steps = 0
        for char in count_s:
            if count_s[char] > count_t[char]:
                steps += count_s[char] - count_t[char]
                
        return steps