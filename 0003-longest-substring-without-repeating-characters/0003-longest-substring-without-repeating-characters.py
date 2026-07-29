class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0

        sliding_window = set()

        while(right < len(s)):

            while (s[right] in sliding_window):
                sliding_window.remove(s[left])
                left += 1
            sliding_window.add(s[right])
            length = right -left +1
            right += 1
            max_length = max(max_length,length)

        return max_length


        