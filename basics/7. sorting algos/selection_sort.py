from typing import List

def find_minimum(array: List[int], i : int) -> int:
    min_index : int = i;    
    for j in range(i, len(array)):
        if array[j] < array[min_index]:
            min_index = j
            
    return min_index

def selection_sort(array: List[int]) -> List[int]:
    for i in range(len(array)):
        min_index = find_minimum(array, i)
        array[i], array[min_index] = array[min_index], array[i]
        
        
    return array


if __name__ == "__main__":
    array : List[int] = [12,4,15,28,9,32]
    
    array = selection_sort(array)
    
    print(array)