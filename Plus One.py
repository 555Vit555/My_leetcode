class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        #result = str(digits)
        result = str(int((''.join(str(digits))[1:-1]).replace(',','').replace(' ',"")) + 1)
        res_list = list(map(int, result))
        return res_list
        #return list(map(int, result))
    

        
    
    
    
    
    
    
digits = [4,3,2,1]
x = Solution().plusOne(digits)
print(x)