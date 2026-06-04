from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        que = deque(students)
        idx = 0       
        skip = 0

        while que and skip < len(que):
          if que[0] == sandwiches[idx]:
              que.popleft()
              idx += 1 
              skip = 0
          else:
              que.rotate(-1)
              skip += 1

        return len(que)

