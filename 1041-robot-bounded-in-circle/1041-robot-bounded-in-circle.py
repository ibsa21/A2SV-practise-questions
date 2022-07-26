class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        move = {'north':(0, 1), 'south':(0, -1), 'west':(-1, 0), 'east':(1, 0)}
        
        clockwise = {'west':'north', 'north':'east', 'east':'south', 'south':'west'}
        anticlockwise = {'west':'south', 'south':'east', 'east':'north', 'north':'west'}
        
        cur_direction = 'north'
        cur_cord = (0, 0)
        for i, inst in enumerate(instructions):
            x, y = cur_cord
            if inst == 'L':
                cur_direction = anticlockwise[cur_direction]
            elif inst == 'R':
                cur_direction = clockwise[cur_direction]
            else:
                xi, yi = move[cur_direction]
                cur_cord = (x + xi, y + yi)
                
        if cur_direction != 'north' or cur_cord == (0, 0): return True
        return False
            