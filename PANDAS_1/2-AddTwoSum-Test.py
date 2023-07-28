def AddTwoSum(nums: list[int], target: int) -> list[int]:
        seen = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff],i]
            else:
                seen[num] = i

#Driver Code
nums=[2,3,7,10,12]
target=9
res=AddTwoSum(nums, target)
print(res)


# diff = target - num
# 7=9 - 2
# 6=9-3
# 2=9-7
#
# #hash_map
# #value index
# 2 0
# 3 1
#
# 0,2

