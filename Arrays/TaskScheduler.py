from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = 0
        completed = items = []
        task_count = Counter(tasks)
        v = max(task_count.values())
        for j in task_count.values():
            if j == v:
                count+=1
        return max(len(tasks), (v-1)*(n+1)+count)
