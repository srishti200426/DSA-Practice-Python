from math import ceil
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''

        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        n = ceil(len(cleaned)/2)
        len_cleaned = len(cleaned)

        for i in range(n):
            if cleaned[i] != cleaned[len_cleaned-i-1]:
                return False
        
        return True



        