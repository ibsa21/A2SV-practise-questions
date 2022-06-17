class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        #changing str of time into minutes
        def findMinute(str_time):
            hr, str_minute = str_time.split(":")
            return int(hr) * 60 + int(str_minute)
        
        emp_time = defaultdict(list)
        
        for i in range(len(keyName)):
            name, time = keyName[i], keyTime[i]
            emp_time[name].append(findMinute(time))
        
        def checkAlarm(time):
            left = 0
            time.sort()
            for right in range(len(time)):
                if time[right] - time[left] <= 60:
                    if right - left >= 2:
                        return True
                else:
                    left += 1
            return False
        
        ans = []
        for emp in emp_time:
            if checkAlarm(emp_time[emp]):
                ans.append(emp)
        ans.sort()
        return ans
