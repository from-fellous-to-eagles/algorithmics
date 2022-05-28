class Solution(object):
    
    
    # author: Saad & Othman
    # time O(n)
    # space O(n)
    def is_anagram_optimal(self, s, t):
        if len(s) == len(t):
            occ = {}
            for c1, c2 in zip(s,t):
                occ[c1] = occ.get(c1, 0) + 1
                occ[c2] = occ.get(c2, 0) - 1
            for _,v in occ.items():
                if v != 0: 
                    return False
            return True
        return False


    # author: Saad & Othman
    # max(len(s), len(t)) := n  
    # time O(nlog(n))
    # space O(1)
    def is_anagram_sol1(self, s, t):
        return sorted(s) == sorted(t)
