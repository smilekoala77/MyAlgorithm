def twoSum(nums, target):
    hash_dic = {}
    for index, val in enumerate(nums):
        hash_key = target - val
        hash_dic[hash_key] = index
    print('hash_dic is ', hash_dic)
    for index, val in enumerate(nums):
        keys = hash_dic.keys()
        if (target - val) in keys:
            return [index, hash_dic[target - val]]
    return


nums = [2,7,11,15]
print(twoSum(nums,9))
