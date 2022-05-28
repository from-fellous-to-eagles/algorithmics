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

    
    # author: Mass
    # time O(n)
    # space O(n)
    def two_sum_sol1(self, nums: List[int], target: int) -> List[int]:
        presentIntegers = defaultdict(lambda: -1)
        for i, number in enumerate(nums):
            presentIntegers[number] = i
        
        for i, number in enumerate(nums):
            if presentIntegers[target - number] > 0 and i != presentIntegers[target - number]  :
                return [i, presentIntegers[target - number]]