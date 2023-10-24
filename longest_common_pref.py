class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # for i in range(len(strs)):
        #     if strs[0][i] != strs[i][i]:
        #         return strs[0][:i]
        #     elif strs[0][0] != strs[1][0]:
        #         return None
        # if strs[0][0] == strs[1][0] == strs[2][0]:
        #     return self.longestCommonPrefix(strs[1:])
        # else:
        
       
            for word in strs:
                if word == "" or strs[0][0] != word[0]:
                    return ''
                            
                for j in range(len(word)):
                    
                    
                    if len(strs) == 1:
                        return word
                    
                    elif strs[0][j] != word[j]:
                        
                        return strs[0][:j]
                    
                       
            
            
            
            
            
            
            
            
        # return strs[0][0]
            
        
        
        
        
        
        









strs1 = ["flower","flow","flight"]
x = Solution().longestCommonPrefix(strs1)
print(x)
print("------------------------------------------------")

str2 = ["dog","racecar","car"]
x = Solution().longestCommonPrefix(str2)
print(x)
print("------------------------------------------------")
strs3=["a"]
x = Solution().longestCommonPrefix(strs3)
print(x)
print("------------------------------------------------")
strs3=[""]
x = Solution().longestCommonPrefix(strs3)
print(x)
print("------------------------------------------------")
strs4 = ["ab", "a"]
x = Solution().longestCommonPrefix(strs3)
print(x)

#print("------------------------------------------------")