from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n>m:
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:n])

        if s1_count == window_count :
            return True

        left = 0
        for right in range(n,m):
            window_count[s2[right]] += 1
            window_count[s2[left]] -=1

            if window_count[s2[left]] == 0:
                del window_count[s2[left]] 

            left += 1

            if s1_count == window_count :
                return True      

        return False