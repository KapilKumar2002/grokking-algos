# Time complexity: O(log n)
# Space complexity: O(1)
# The array should be sorted array


from typing import Optional, List

def binary_search(array: List[int], x : int) -> Optional[int]:
    l : int = 0
    h : int = len(array) - 1
    
    while l <= h:
        mid : int = l+(h-l)//2
        guess = array[mid]
        if guess == x:
            return mid
        
        elif guess > x:
            h = mid - 1
            
        else:
            l = mid + 1
            
    return None


if __name__ == "__main__":
    array : List[int] = [2,4,5,8,9,12]
    x : int = 9
    
    result : Optional[int] = binary_search(array, x)
    
    print(result)