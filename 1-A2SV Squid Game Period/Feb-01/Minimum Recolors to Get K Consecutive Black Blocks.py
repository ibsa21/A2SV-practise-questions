class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        answer = k
        black_count = 0
        white_count = 0
        left_pointer = 0

        for right_pointer, color in enumerate(blocks):
            if color == 'W':
                white_count += 1
            else:
                black_count += 1

            if right_pointer - left_pointer + 1==k:
                answer = min(answer, k - black_count)
                if blocks[left_pointer] == 'W':
                    white_count -= 1
                else:
                    black_count -= 1
                left_pointer += 1
        return answer
