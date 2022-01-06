class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        if secret == guess:
            return str(len(guess)) + "A0B"
        
        bulls = 0
        cows = 0
        newS  =[]
        newG = []
        for i in range(len(secret)):
            if int(secret[i])==int(guess[i]):
                print(guess[i], secret[i])
                bulls +=1
            else:
                newG.append(guess[i])
                newS.append(secret[i])
         
        for k in newG:
            if k in newS:
                cows += 1
                newS.remove(k)
        return str(bulls) + 'A' + str(cows) +'B'
                
