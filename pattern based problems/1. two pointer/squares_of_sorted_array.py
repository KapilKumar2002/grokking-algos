from typing import List
def square_of_sorted_array(nums : List[int]):
    i : int = 0
    j : int = len(nums) - 1
    
    while i<=j:
        l = nums[i] ** 2
        r = nums[j] ** 2
        
        if l > r:
            temp:int = nums[j]
            nums[j] = l
            nums[i] = temp
            j-=1
        elif l < r:
            nums[j] = r
            j-=1
        else:
            nums[i] = l
            nums[j] = r
            i+=1
            j-=1
    
    
    
if __name__ == "__main__":
    nums : List[int] = [-4,-1,0,3,10]
    nums : List[int] = [-7,-3,2,3,11]
    
    square_of_sorted_array(nums)
    
    print(nums)