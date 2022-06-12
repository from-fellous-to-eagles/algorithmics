class Solution:

    # author: NeetCode
    # n:= len(strs), m:= max(len(s))
    # time O(n*m)
    # space O(n)
    def group_anagrams_optimal(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1 
            res[tuple(count)].append(s)

        return res.values()
    
    
    # author: Saad, Othman & Mass
    # time O(n^2log(n))
    # space O(n)
    def group_anagrams_sol1(self, strs: List[str]) -> List[List[str]]:
        hashlist = defaultdict(list)
        for w in strs:
            hashlist[str(sorted(w))].append(w)
            
        return hashlist.values()