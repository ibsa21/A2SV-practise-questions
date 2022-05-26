class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser_winner = defaultdict(set)
        for winner, loser in matches:
            loser_winner[loser].add(winner)
        zero_lose = set()

        for winner, loser in matches:
            if winner not in loser_winner:
                zero_lose.add(winner)
        one_lose =  [key for key in loser_winner if len(loser_winner[key])==1]
        
        zero_lose = list(zero_lose)
        zero_lose.sort()
        one_lose = list(one_lose)
        one_lose.sort()
        return [zero_lose, one_lose]