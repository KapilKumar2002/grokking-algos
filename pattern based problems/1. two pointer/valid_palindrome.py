from typing import List
def valid_palindrome(nums: List[int]) -> bool:
    i : int = 0
    j : int = len(nums) - 1
    
    while i<=j:
        if(nums[i] != nums[j]):
            return False
        
        i+=1
        j-=1
        
    return True
        
    
    
if __name__ == "__main__":
    nums : List[int] = [1,1,3,2,1]
    
    print(valid_palindrome(nums))