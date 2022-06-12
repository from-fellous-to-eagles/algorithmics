class Solution:

    # author: Neetcode
    # time: O(n)
    # space: O(n)
    def top_k_frequent_optimal(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
    
    # author: Saad
    # time: O(nlog(n))
    # space: O(n)
    def top_k_frequent_sol1(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(lambda: 0)
        for n in nums:
            count[n] += 1
        return [k for k,v in sorted(count.items(), key=lambda pair: pair[1], reverse=True)][:k]