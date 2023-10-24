class Solution:
    def romanToInt(self, s: str) -> int:
        val_list = [1, 5, 10, 50, 100, 500, 1000]
        
        # digit = 0
        # for i, symbol in enumerate(s): 
        #     if symbol == 'M' and s[i-1] != 'C' or symbol == s[:-1]:
        #         digit = digit + 1000
                
        #     elif symbol == 'M' and s[i-1] == 'C' or symbol == s[:-1]:
        #         digit = digit + 900
                
        #     elif symbol == 'D' and s[i-1] != 'C' or  symbol == s[:-1]:
        #         digit = digit + 500
                
        #     elif symbol == 'D' and s[i-1] == 'C' or  symbol == s[:-1]:
        #         digit = digit + 400
                
        #     elif symbol == 'C' and s[i-1] != 'X' and s[i+1] != 'M' and s[i+1] != 'D' or  symbol == s[:-1]:
        #         digit = digit + 100
                
        #     elif symbol == 'C' and s[i-1] == 'X' and s[i+1] != 'M' and s[i+1] != 'D' or  symbol == s[:-1]:
        #         digit = digit + 90
                
        #     elif symbol == 'L' and s[i-1] != 'X' or  symbol == s[:-1]:
        #         digit = digit + 50
                
        #     elif symbol == 'L' and s[i-1] == 'X' or  symbol == s[:-1]:
        #         digit = digit + 40
                
        #     elif symbol == 'X' and s[i-1] != 'I' and s[i+1] != 'C' or symbol == s[:-1]:
        #         digit = digit + 10
                
        #     elif symbol == 'X' and s[i-1] == 'I' and s[i+1] != 'C' or  symbol == s[:-1]:
        #         digit = digit + 9
                
        #     elif symbol == 'V' and s[i-1] != 'I' or symbol == s[:-1]:
        #         digit = digit + 5
        #     elif symbol == 'V' and s[i-1] == 'I' or  symbol == s[:-1]:
        #         digit = digit + 4
                
        #     elif symbol == 'I' and s[i-1] != 'V' or  symbol == s[:-1]:
        #         digit = digit + 1
        #     continue
            
        #return digit
        #dict_rul = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        dict_rul ={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            if i < len(s) - 1 and dict_rul[s[i]] < dict_rul[s[i+1]]:
                result -= dict_rul[s[i]]
            else:
                result += dict_rul[s[i]]
        return result

x = Solution().romanToInt("MCMXCIV")
print(x)    