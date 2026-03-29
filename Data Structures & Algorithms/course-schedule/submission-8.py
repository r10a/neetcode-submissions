from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        
        adjacency_set = defaultdict(set)
        for a, b in prerequisites:
            adjacency_set[b].add(a)
        queue = deque()
        courses_seen = set()
        for course in adjacency_set.keys():
            if course in courses_seen:
                continue
            
            queue.append(course)
            visited = set([course])
            while queue:
                curr = queue.popleft()
                if curr not in adjacency_set:
                    continue
                for future_course in adjacency_set[curr]:
                    if future_course in visited:
                        return False
                    if future_course in adjacency_set:
                        queue.append(future_course)
                        visited.add(future_course)
            courses_seen |= visited
        return True
