from typing import List, Optional

def container_with_most_water(height: List[int]) -> Optional[int]:
    l: int = 0
    r: int = len(height)-1
    area : int = -1000
    
    while l <= r:
        h : int = min(height[l],  height[r])
        w : int = abs(l - r)
        cal_area = h * w
        area = max(area, cal_area)
        if l < r:
            l+=1
        elif l > r:
            r-=1
        else:
            l += 1
            r -= 1
        
    return area
        

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    
    print(container_with_most_water(height))
    
    
    