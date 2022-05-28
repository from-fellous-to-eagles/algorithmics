class Solution(object):

    # author: Saad & Othman
    # time O(n)
    # space O(n)
    def two_sum_optimal(self, nums, target):
        d = {}
        for i,n in enumerate(nums):
            diff = target - n
            
            if diff in d:
                return [d[diff], i]
            else:
                d[n] = i

