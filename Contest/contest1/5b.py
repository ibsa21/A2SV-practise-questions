number = int(input("Enter number: "))
string = []
while(number !=0 ):
    number-= 1
    remainder = number % 26
    string.append(chr(remainder + 65))
    number = number // 26
    
print("".join(reversed(string)))
