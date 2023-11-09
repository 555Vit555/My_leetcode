class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        
        dict = {}
      
        dict = {num: (nums.count(num))-1 for num in nums}        
      
        i = sum (dict.values())
        result = list(dict.keys())
        # for g in range(i):
        #     result.append('_')
        #nums = int(str(list(dict.keys())).replace(']','') + (",_")*i + "]")
        
        #return i, f'nums = {nums}'
        return result
      # g = ''
        # for num in nums:
        #     #i = nums.count(num) -1
        #     #if nums.count(num) > 1:
        #     if g != num:
        #         #i = nums.count(num) -1
                
        #         i += nums.count(num) - 1
        #             # while num in nums:  
        #             #     nums.remove(num)
                
        #     # nums1.append(num)
        #     g = num        
                
        #dict = dict(enumerate(nums))
  #result = str(nums1).replace(']','') + (",_")*i + "]"
#print(f'{i+1}, {result}')

# print(f'{i}, {result}')





nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
#nums = [1,1,1,1]
x = Solution().removeDuplicates(nums)
print(x)
# ii = 0
        
        dict = {}
      
        dict = {num: (nums.count(num))-1 for num in nums}        
      
        i = sum (dict.values())
        #nums = str(list(dict.keys())).replace(']','') + (",_")*i + "]"
        result = list(dict.keys())
        for g in range(i):
            result.append('_')
        return i, result