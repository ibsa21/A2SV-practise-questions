class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        """
        R:5 R:6
        D:4
        
        """
        
        radiants, dires = deque(), deque()
        
        for index, senator in enumerate(senate):
            if senator == "R":
                radiants.append(index)
            elif senator == "D":
                dires.append(index)
        
        while radiants and dires:
            radiant, dire = radiants.popleft(), dires.popleft() 
            if radiant < dire:
                radiants.append(radiant + len(senate))
            elif radiant > dire:
                dires.append(dire + len(senate))
        
        return "Radiant" if radiants else "Dire"