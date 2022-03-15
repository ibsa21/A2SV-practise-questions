from itertools import count

test_case = int(input())

for  _ in range(test_case):

    target = int(input())

    def calculate(start):
        count = 0
        while start < target:
            start += 4
            count +=1
        
        while start > target:
            start -=1 
            count +=1 
        return count
    
    count_one = calculate(31)
    count_two  = calculate(32)

    if count_one <= count_two:
        print(31)
    else:
        print(32)