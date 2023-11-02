class Solution:
    def isValid(self, s: str) -> bool:
        param = {
            '(':')',
            '[':']',
            '{':'}'
        }
        # param_open = ['(','[','{']
        # param_close = [')',']','}']
        # for i in range(len(s)):
        #     for k, v in param.items():
        #         if s[i] == k and v in s:
        #             return True
        #         else:
        #             return False
            
            
            # if s[i] in param_close and s[i-1] in param_open:
            #    return True
        for symb in s:
            count = s.count(symb)
            
       










s = "()"
x = Solution().isValid(s)
print(x) 
print('-------------------------------------------------------------------')
s1 ="(]"
x = Solution().isValid(s1)
print(x) 
print('-------------------------------------------------------------------')
s = "{[]}"
x = Solution().isValid(s1)
print(x) 
print('-------------------------------------------------------------------')