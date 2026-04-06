from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            counter = [0] * 26
            for letter in word:
                counter[ord(letter) - ord('a')] += 1
            key = tuple(counter)
            ans[key].append(word)
        return list(ans.values())
        