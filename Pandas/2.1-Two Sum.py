def AddTwoSum(nums, target):
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return([seen[target - num], i])
            elif num not in seen:
                seen[num] = i


#nums=[2,3,7,10,11]
nums=[2,1,5,3]
target=4
res=AddTwoSum(nums,target)
print(res)
