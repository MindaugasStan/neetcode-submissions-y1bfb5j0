# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        result = []
        if not pairs:
            return result
        result.append(pairs[:])
        for i in range(1, n):
            j = i - 1
            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                res = pairs[j]
                pairs[j] = pairs[j+1]
                pairs[j+1] = res
                j -= 1
            result.append(pairs[:])
        return result
  
