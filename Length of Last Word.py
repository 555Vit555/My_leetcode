class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s_list = list(filter(None, s.split(' ')))
        
        return len(s_list[-1])
        
        







#s = "Hello World"
# x = Solution().lengthOfLastWord(s)
# print(x)
#s = "   fly me   to   the moon  "
s = "luffy is still joyboy"
x = Solution().lengthOfLastWord(s)
print(x)