from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        hashmap = defaultdict(int)

        for i in range(len(s)):
            hashmap[s[i]] += 1
            hashmap[t[i]] -= 1
        
        return all(v == 0 for v in hashmap.values())

        