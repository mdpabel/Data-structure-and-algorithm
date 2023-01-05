# https://leetcode.com/problems/repeated-dna-sequences/

mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
base = 4

def hashFunc(char, exp):
    return mapping.get(char) * pow(base, exp) 

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        window_size = 10
        n = len(s)
        
        if n <= window_size:
            return []
         
        hashing = 0
        seen, result = set(), set()
        
        for i in range(n - window_size + 1):
            if i != 0:
                hashing = ((hashing - hashFunc(s[i-1], window_size-1)) * base)  + hashFunc(s[window_size + i - 1], 0)
            else:
                for j in range(window_size):
                    hashing += hashFunc(s[j], window_size - j - 1)
                    
            if hashing in seen:
                result.add(s[i:i+window_size])
            seen.add(hashing)
 

        return result