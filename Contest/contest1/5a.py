alphabetDict = {}
for i in range(65, 91):
    alphabetDict[chr(i)] =  (26 - (90 - ord(chr(i))))

letter = input("Enter a word: ")
value = 0
letter = list(reversed(letter))
for i in range(len(letter)):
    print(letter[i])
    value += pow(26, i) * alphabetDict[letter[i]]
print(value)
