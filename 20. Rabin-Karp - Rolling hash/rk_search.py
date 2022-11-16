""" 
https://www.youtube.com/watch?v=V5-7GzOfADQ&t
"""

con = 26
    
def hashFunc(char, exp):
    return (ord(char) - ord('a') + 1) * pow(con, exp) 

def rk_search(string, pattern):
    len_str = len(string)
    len_pat = len(pattern)
    
    pat_hash = 0
    curr_str_hash = 0
    
    for i in range(len_pat):
        pat_hash += hashFunc(pattern[i], len_pat - i - 1)
        curr_str_hash += hashFunc(string[i], len_pat - i - 1)
        
    for i in range(len_str - len_pat + 1):
        if i > 0:
            curr_str_hash = ((curr_str_hash - hashFunc(string[i-1], len_pat - 1)) * con) + hashFunc(string[i + len_pat - 1], 0)
        
        if curr_str_hash == pat_hash:
            print(string[i:i+len_pat] == pattern)
    
rk_search("abcdefg", "cde")