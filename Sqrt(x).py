class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i*i <=x :
            if (i+1)*(i+1) > x:
                return i
            else:i += 1
            
        
           
        





#x = 4
x = 8
x = 16
y = Solution().mySqrt(x)
print(y)