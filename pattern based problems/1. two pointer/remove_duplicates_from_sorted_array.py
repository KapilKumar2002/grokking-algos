from typing import List

def remove_duplicates_from_sorted_array(nums : List[int]):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i+=1
            nums[i] = nums[j]  
            
    
if __name__ == "__main__":
    nums : List[int] = [0,0,1,1,1,2,2,3,3,4]
    
    remove_duplicates_from_sorted_array(nums)
    
    print(nums)
    
    
    
# time complexity
# O(n)