class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"
        special_numbers = {1:"Thousand", 2:"Million", 3:"Billion"}
        numbers  = {0:'',1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine",10: "Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 20:"Twenty", 30:"Thirty",40 :"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety"
        }

        def insert_word(num, index, word):
            if int(num[index]) == 1:
                word.append(numbers[int(num[index:])])
            else:
                word.append(numbers[int(num[index]+'0')])
                word.append(numbers[int(num[index+1])])

        def sayWord(num, house):
            word = []

            if len(num) == 1:
                word.append(numbers[int(num[0])])
            elif len(num) == 2:
                insert_word(num, 0, word)
            else:
                word.append(numbers[int(num[0])])
                if int(num) != 0:
                    word.append('Hundred')
                insert_word(num, 1, word)

            if house and int(num) != 0:word.append(special_numbers[house])
            return ' '.join([char for char in word if char]).strip()

        num = str(num)
        group_count = 0
        answer = []
        for i in range(len(num)-1, -1, -3):
            current_num = num[max(0, i-2):i+1]
            temp = sayWord(str(int(current_num)), group_count)
            if temp:answer.append(temp)
            group_count += 1
        return ' '.join(answer[::-1]).strip()