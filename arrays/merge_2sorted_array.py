class Solution:
    def mergeArrays(self, a, b):

        n = len(a)
        m = len(b)

        gap = (n + m + 1) // 2

        while gap > 0:

            left = 0
            right = left + gap

            while right < n + m:

                # both pointers in a
                if left < n and right < n:
                    if a[left] > a[right]:
                        a[left], a[right] = a[right], a[left]

                # left in a, right in b
                elif left < n and right >= n:
                    if a[left] > b[right - n]:
                        a[left], b[right - n] = b[right - n], a[left]

                # both pointers in b
                else:
                    if b[left - n] > b[right - n]:
                        b[left - n], b[right - n] = b[right - n], b[left - n]

                left += 1
                right += 1

            if gap == 1:
                break

            gap = (gap + 1) // 2