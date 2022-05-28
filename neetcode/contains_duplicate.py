class Solution(object):
    
    # author: Saad, Othman & Mass
    # time O(n)
    # space O(n)
    def contains_duplicate_optimal(self, nums):
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False
