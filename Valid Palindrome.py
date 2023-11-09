class Solution:
    def isPalindrome(self, s: str) -> bool:
        #string_s = s.lower().replace(' ','').replace(',','').replace(':','').replace('.','').replace('@','').replace('#','').replace('_','')
        string_s = ''.join(c for c in s if c.isalpha() or c.isdigit()).lower()
        #string_s = ''.join(c for c in s if c.isalpha() or c.isdigit()).lower()
        print(string_s)
        if string_s[0::] == string_s[::-1]:
            return True
        else:
            return False







s = "A man, a plan, a canal: Panama"
x= Solution().isPalindrome(s)
print(x)