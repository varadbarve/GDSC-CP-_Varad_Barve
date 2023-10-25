def find_quadruplets(nums, target):
    nums.sort()
    
    quadruplets = set()
    
    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            for k in range(j + 1, len(nums) - 1):
                for l in range(k + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        quadruplets.add((nums[i], nums[j], nums[k], nums[l]))
    
    return list(quadruplets)

nums = input("Enter the numbers from which the quadruplet is to be sorted (separated by spaces): ")
nums = [int(x) for x in nums.split()]          
target = int(input("Enter the target value: "))

print(find_quadruplets(nums, target))