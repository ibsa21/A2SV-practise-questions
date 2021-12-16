if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arrList = list(arr)
    count = arrList.count(max(arrList))
    arrList.sort()
    print(arrList[len(arrList)-(count + 1)])
    
