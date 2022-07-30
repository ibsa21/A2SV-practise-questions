from itertools import permutations
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        ''''''
        def is_match(word:str)->bool:
            counter = Counter(word)
            for key in joined_pattern:
                if key not in counter or counter[key] < joined_pattern[key]: return False
            return True
        
        joined_pattern = defaultdict(int)
        for word in words2:
            for key, value in Counter(word).items():
                joined_pattern[key] = max(joined_pattern[key],value)
        
        return [word for word in words1 if is_match(word)==True]
    
        #bruteforce
        #step1: store all the subsets of an element
        subset_dict  = defaultdict(set)
        for word in words1:
            for r in range(1, len(word) + 1):
                for subset in permutations(word, r):
                    subset_dict[word].add(''.join(subset))
                
        for word in words2:
            deleted = []
            for key in subset_dict:
                if word not in subset_dict[key]:
                    deleted.append(key)
            for char in deleted: del subset_dict[char]
        
        return [key for key in subset_dict]