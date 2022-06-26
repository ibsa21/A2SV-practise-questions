class TrieNode:
    def __init__(self, digit:str = ''):
        self.children:Dict[str, Dict] = {}
        self.digit = digit
        self.is_end:bool = False
        
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        root = TrieNode()
        
        def insert(alphanum:str)->None:
            cur_root:TrieNode = root
            for digit in alphanum:
                if digit not in cur_root.children:
                    cur_root.children[digit] = TrieNode(digit)
                cur_root = cur_root.children[digit]
            cur_root.is_end = True
        
        for num in range(1, n + 1):
            insert(str(num))
        
        ans = []
        def dfs(node, cur_num):
            if cur_num != '0':ans.append(int(cur_num))
            for child in node.children:
                dfs(node.children[child], cur_num + child)
        dfs(root, '0')
        return ans
            
        """
            time complexity: O(nlogn)
            space complexity: O(n)
        """
        nums = [str(num) for num in range(1, n + 1)]
        nums.sort()
        return list(map(int, nums))
