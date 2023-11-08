class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for num in nums:
            if nums.count(num) > 1:
                nums.remove(num)
                i +=1
        nums.append('_'*i)
        print(f'{i}, {nums}')









nums = [1,1,2]
x = Solution().removeDuplicates(nums)
