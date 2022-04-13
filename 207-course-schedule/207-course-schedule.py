class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        """
        steps:
        1. find number of courses that has prerequisites - > count_course
        2. add course and it's prerequisites in dictionary 
        3. add courses that does not have prerequisites in queue
        4. do bfs for courses that are in queue
        """
        #number of prerequisites for each courses
        no_preq = [0] * numCourses
        
        #course and it's preq
        preq_course = defaultdict(set)
        
        for course, preq in prerequisites:
            no_preq[course] += 1
            preq_course[preq].add(course)
            
        
        #add course index  that does not have preq
        queue = deque()
        
        for i in range(numCourses):
            if no_preq[i]==0:
                queue.append(i)
        
        
        course_taken = 0
        while queue:
            course = queue.popleft()
            course_taken += 1
            
            for course_preq in preq_course[course]:
                no_preq[course_preq] -= 1
                
                if no_preq[course_preq]==0:
                    queue.append(course_preq)
            
            
        
        return course_taken == numCourses
        