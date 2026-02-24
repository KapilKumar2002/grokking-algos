from typing import List, Optional, DefaultDict
from collections import defaultdict

def maximum_sum_subarray(nums: List[int], k:int) -> Optional[int]:
    sum :int = 0
    j : int = 0
    window_sum: int = 0
    elements : DefaultDict[int, int] = defaultdict(int)
    for i in range(len(nums)):
        window_sum+= nums[i]
        elements[nums[i]]+=1
        
        if i - j + 1 > k:
            window_sum -= nums[j]
            j+=1
            elements[nums[j]]-=1
            if elements[nums[j]]==0:
                elements.pop(nums[j])
            
        
        if len(elements) == k and i - j + 1 == k:
            sum = max(sum, window_sum)
            
    return sum


if __name__ == "__main__":
    nums : List[int]  = [1,5,4,2,9,9,9]
    k = 3
    print(maximum_sum_subarray(nums, k))