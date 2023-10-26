class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
       
        
            if not strs:
                return ''
            for word in strs:
                if word == "" or strs[0][0] != word[0]:
                    return ''
                            
                for j in range(len(word)):
                    
                    #if strs[0][j+1] :
                        if len(strs) == 1:
                            return word
                        # elif word == 1:
                        #     return strs[0][:j]
                        
                        elif strs[0][j] != word[j]:
                            
                            return strs[0][:j]
            # if not strs:
            #     return ''
            
            
            # # result = ''
            
            # # for i in range(len(strs)):
            # #     for j in range(len(min(strs))):
            # #         if strs[0][j] == strs[i][j]:
            # #             result += strs[0][j]
            # # return result
            # result = ""
            # for j in range(len(strs[0])):
            #     if len(strs[0]) >= len(strs[j]):
            #         for i in range(1, len(strs)):
                    
            #             if strs[0][j] != strs[i][j]:
            #                 return result
                    
            #     result += strs[0][j]
            # return result            
                        
                    
                        
                        
            
                    
                    #if strs[0][j+1] :
                        
                        # elif word == 1:
                        #     return strs[0][:j]
                        
                       
                    
            
            
            
            
            
            
            
            
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
x = Solution().longestCommonPrefix(strs4)
print(x)

print("------------------------------------------------")
# strs4=["ab","a"]
# x = Solution().longestCommonPrefix(strs4)
# print(x)
# print("------------------------------------------------")