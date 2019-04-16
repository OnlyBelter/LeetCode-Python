# python 3.6

# solution 1
# 直接遍历
# 缺点：特别耗时，时间复杂度高
# 优点：
# time: 7952 ms, memory: 13.7 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(i+1, len_nums):
                if nums[i] + nums[j] == target:
                    return [i, j]


# solution 2
# 使用字典存储，且需要避免重复使用同一个元素
# 缺点：
# 优点：高效
# time: 80 ms, memory: 14.2 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       if not nums:
           return None
       d = dict()
       for i, item in enumerate(nums):
           tmp = target - item
           if tmp in d:
               return [d[tmp], i]
           d[item] = i

       return None
