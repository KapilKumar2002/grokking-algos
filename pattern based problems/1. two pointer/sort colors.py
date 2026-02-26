# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n : int = len(nums)
        low : int = 0
        high : int = n - 1
        mid : int = 0

        while mid <= high:
            num = nums[mid]
            
            if nums == 0:
                nums[mid] = nums[low]
                nums[low] = num
                low += 1
                mid += 1 

            elif num == 2:
                nums[mid] = nums[high]
                nums[high] = num
                high -= 1
            
            else:
                mid += 1



if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    solution = Solution()
    solution.sortColors(nums)
    print(nums)