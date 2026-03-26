class DSU: 
    def __init__(self, n: int) -> None: 
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_groups = n

    def find(self, i: int) -> int: 
        if self.parent[i] == i: 
            return i
        
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i: int, j: int) -> bool: 
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j: 
            return False
        
        if self.size[root_i] > self.size[root_j]:
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
        else: 
            self.parent[root_i] = root_j
            self.size[root_j] += self.size[root_i]
        
        return True

class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        mask_to_idx = {}

        dsu = DSU(len(words))

        def get_mask(word: str) -> int: 
            mask = 0
            for ch in word: 
                bit_position = ord(ch) - ord('a')
                mask = mask | 1 << bit_position
            
            return mask

        for i in range(len(words)):
            mask = get_mask(words[i]) 

            if mask in mask_to_idx: 
                if dsu.union(i, mask_to_idx[mask]):
                    dsu.num_groups -= 1
            else: 
                mask_to_idx[mask] = i

        for original_mask, i in mask_to_idx.items(): 
            for j in range(26):
                if (original_mask & (1 << j)) == 0:
                    neighbor_mask = original_mask | (1 << j)
                    
                    if neighbor_mask in mask_to_idx:
                        if dsu.union(i, mask_to_idx[neighbor_mask]):
                            dsu.num_groups -= 1

            for j in range(26):
                if (original_mask & (1 << j)) != 0:
                    neighbor_mask = original_mask ^ (1 << j)
                    
                    if neighbor_mask in mask_to_idx:
                        if dsu.union(i, mask_to_idx[neighbor_mask]):
                            dsu.num_groups -= 1

            for j in range(26):
                if (original_mask & (1 << j)) != 0:
                    for k in range(26):
                        if (original_mask & (1 << k)) == 0:
                            neighbor_mask = (original_mask ^ (1 << j)) | (1 << k)
                            
                            if neighbor_mask in mask_to_idx:
                                if dsu.union(i, mask_to_idx[neighbor_mask]):
                                    dsu.num_groups -= 1    
        
        return [dsu.num_groups, max(dsu.size)]
