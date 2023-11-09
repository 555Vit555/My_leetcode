class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in nums:
            if i >= target and target <= nums[-1]:
                
                return nums.index(i)
            elif target > nums[-1]:
                nums.append(target)
                return nums.index(target)
        
nums = [1,3,5,6]
target = 5
x = Solution().searchInsert(nums, target)
print(x)
nums = [1,3,5,6]
target = 2
x = Solution().searchInsert(nums, target)
print(x)

nums = [1,3,5,6]
target = 7
x = Solution().searchInsert(nums, target)
print(x)