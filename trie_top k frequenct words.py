class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.end_word = False
        self.word = ''
        self.freq = 0
    
    def __lt__(self, a):
        return self.freq > a.freq if self.freq != a.freq else self.word < a.word        
        
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        trie_data = TrieNode()
        
        #build trie data structure
        def insert(word):
            root = trie_data
            
            for char in word:

                if char not in root.children:
                    root.children[char] = TrieNode()

                root = root.children[char]

            root.word = word
            root.freq += 1
            root.end_word = True
        
        #insert each words into trie
        for word in words:
            insert(word)
            
        #find the element with highest frequency and smallest lexicographical order if the same frequency
        def return_highest(k:int, root):

            queue, pq = deque([root]), []

            while queue:
                node = queue.popleft()

                if node.end_word:
                    heapq.heappush(pq, node)

                for key in node.children:
                    queue.append(node.children[key])

            result_node = heapq.nsmallest(k, pq)
            return [node.word for node in result_node]
        return return_highest(k, trie_data)
    
