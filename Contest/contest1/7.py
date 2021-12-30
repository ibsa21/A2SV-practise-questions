romanNumber = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}

total = 0
romanValue = input()
for i in range(1,len(romanValue)):
    if romanNumber[romanValue[i-1]] < romanNumber[romanValue[i]]:
        total -= romanNumber[romanValue[i-1]]
    else:
        total += romanNumber[romanValue[i-1]]
    
total+=romanNumber[romanValue[-1]] #adding the last digit to resul
print(total)