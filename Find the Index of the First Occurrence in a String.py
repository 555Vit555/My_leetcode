class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1



haystack = "sadbutsad"
needle = "sad"
x = Solution().strStr(haystack, needle)
print(x)
haystack = "leetcode"
needle = "leeto"
x = Solution().strStr(haystack, needle)
print(x)