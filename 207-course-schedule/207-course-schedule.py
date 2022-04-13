class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        count_course = [0] * numCourses
        
        preq_course = defaultdict(set)
        
        for course, req in prerequisites:
            count_course[course] += 1
            preq_course[req].add(course)
        
        queue = deque()
        
        for i in range(numCourses):
            if count_course[i]==0:
                queue.append(i)
        
        course_taken = 0
        while queue:
            course = queue.popleft()
            course_taken += 1
            
            for courses in preq_course[course]:
                count_course[courses] -= 1
                
                if count_course[courses] == 0:
                    queue.append(courses)
        
        return course_taken == numCourses
            