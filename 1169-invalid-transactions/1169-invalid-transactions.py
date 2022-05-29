class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        trax_dict = defaultdict(list)
        
        for i in range(len(transactions)):
            name, mins, money, city  = transactions[i].split(',')
            trax_dict[name].append((int(mins), city))
            
        invalid = list()
        for i in range(len(transactions)):
            name, mins, money, city  = transactions[i].split(',')
            if int(money) > 1000:
                invalid.append(transactions[i])
            else:
                for j in range(len(trax_dict[name])):
                    t_mins, t_city = trax_dict[name][j]
                    
                    if city!=t_city and abs(int(mins)-t_mins) <= 60:
                        invalid.append(transactions[i])
                        break
        return invalid
                