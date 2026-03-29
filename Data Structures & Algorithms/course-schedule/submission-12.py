class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency_list = defaultdict(list)
        for a, b in prerequisites:
            adjacency_list[b].append(a)
        
        for course in adjacency_list.keys():
            stack = [course]
            visited = set([course])
            while stack:
                curr = stack.pop()
                if curr not in adjacency_list:
                    continue
                for dependency in adjacency_list[curr]:
                    if dependency not in adjacency_list:
                        continue
                    # cycle detected
                    if dependency in visited:
                        return False
                    visited.add(dependency)
                    stack.append(dependency)
        return True
