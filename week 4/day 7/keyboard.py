t = int(input())
for _  in range(t):
    alphabet = str(input())
    word = str(input())
    result = 0
    for i in range(len(word)-1):
        result += abs(alphabet.index(word[i]) - alphabet.index(word[i+1]))
    print(result)
        

