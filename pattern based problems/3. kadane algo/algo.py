from typing import List, Optional

def kadane_algo(nums: List[int]) -> Optional[int]:
    sum: int = 0
    temp: int = 0
    
    for i in range(len(nums)):
        temp += nums[i]
        
        sum = max(sum, temp)
        
        if temp < 0:
            temp = 0
            
    return sum


if __name__ == "__main__":
    nums : List[int] = [-2,1,-3,4,-1,2,1,-5,4]
    print(kadane_algo(nums))