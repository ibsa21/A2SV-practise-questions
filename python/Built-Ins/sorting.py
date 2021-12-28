# Enter your code here. Read input from STDIN. Print output to STDOUT
S = input()
oddNumber = []
evenNumber = []
lowercase = []
uppercase = []
for i in S:
    if i.isdigit():
        if int(i) % 2 == 0:
            evenNumber.append(i)
        else:
            oddNumber.append(i)
    elif i.isalpha():
        if i.islower():
            lowercase.append(i)
        else:
            uppercase.append(i)
lowercase.sort()
uppercase.sort()
oddNumber.sort()
evenNumber.sort()
newString = lowercase + uppercase + oddNumber + evenNumber
print("".join(newString))
