from collections import defaultdict

def valid_anagram(s:str, t: str) -> bool:
    if len(s) != len(t):
        return False
    seen = defaultdict(int)
    
    for i in s:
        seen[i]+=1
        
    for i in t:
        seen[i]-=1
        if seen[i] <0:
            return False
        
    for value in seen.values():
        if value != 0:
            return False
        
    return True


# def valid_anagram(s:str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
#     seen = defaultdict(int)
#     teen = defaultdict(int)
    
#     for i in range(len(s)):
#         seen[s[i]]+=1
#         teen[t[i]]+=1
        
#     for i in s:
#         if(seen[i] != teen[i]):
#             return False
        
#     return True
        
    

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    
    print(valid_anagram(s,t))