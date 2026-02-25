from typing import List

def subarray_sum_equal_k(nums: List[int], k : int):
    n = len(nums)
    prefix_sum = [0]*n
    suffix_sum = [0]*n
    prefix_sum[0] = nums[0]
    suffix_sum[n - 1] = nums[n - 1]
    
    ans : int = 0
    
    for i in range (1, n):
        prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
    for i in range (1, n):
        suffix_sum[n-i-1] = suffix_sum[n-i] + nums[n-i-1]
        
    for i in range(0,n):
        if prefix_sum[i] == k or suffix_sum[i]==k:
            ans += 1
            
            
    return ans
    
    
if __name__ == "__main__":
    nums = [1,2,1,2,1,3]
    k = 6
    ans = subarray_sum_equal_k(nums, k)
    print(ans)
    
    