from typing import Optional, DefaultDict
from collections import defaultdict

def longest_sub_string(s:str)-> Optional[int]:
    l : int = 0
    ans: int = 0
    elements : DefaultDict[str, int] = defaultdict(int)
    for i in range(len(s)):
        if elements[s[i]] >= l:
            l = elements[s[i]] + 1
        elements[s[i]]=i
        val:int = i - l + 1
        ans = max(ans,val)
        
    return ans
        
    
if __name__ == "__main__":
    s : str = "bbbbb"
    print(longest_sub_string(s))