class Solution:

    # author: Saad
    # time: O(nlog(n))
    # space: O(n)
    def top_k_frequent_sol1(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(lambda: 0)
        for n in nums:
            hash[n] += 1
        return [k for k,v in sorted(hash.items(), key=lambda pair: pair[1], reverse=True)][:k]