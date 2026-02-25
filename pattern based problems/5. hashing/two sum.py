from typing import List, Optional
from collections import defaultdict

def two_sum(nums : List[int], target: int)-> Optional[List[int]]:
    map = {}
    for i in range(len(nums)):
        second_ele : int = target - nums[i]
        if second_ele in map:
            return [map[second_ele], i]
        else:
            map[nums[i]] = i
    
    return None


if __name__ == "__main__":
    nums: List[int] = [2,7,11,15]
    target:int = 9
    print(two_sum(nums, target))