number = int(input("Enter number: "))
string = []
while(number != 0):
    remainder = number % 26
    string.append(chr(remainder + 64))
    number = number // 16

print("".join(reversed(string)))