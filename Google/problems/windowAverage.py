def windowAverge(nums, k):
    sum_k = sum(nums[:k])
    res = [sum_k / k]
    for i in range(len(nums) - k):
        sum_k = sum_k - nums[i] + nums[i+k]
        print sum_k
        res.append(sum_k * 1.0 / k)
    return res


print windowAverge([1,2,3,4,5,6,7], 2)