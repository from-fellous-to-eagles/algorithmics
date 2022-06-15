class Solution:

    # author: Neetcode
    # time O(n)
    # space O(1)
    def product_except_self_optimal(self, num: List[int]) -> List[int]:
        res = [1] * len(num)
        prefix = 1
        for i in range(len(num)):
            res[i] = prefix
            prefix *= num[i]
        
        postfix = 1
        for i in range(len(num)-1, -1, -1):
            res[i] *= postfix
            postfix *= num[i]

            
        return res
    

    # author: Saad
    # time O(n)
    # space O(1)
    # less readable than ci-dessus
    def product_except_self_optimal1(self, num: List[int]) -> List[int]:
        res = [1] * len(num)
        res[1] =  num[0]
        
        for i in range(2, len(num)):
            res[i] = res[i-1] * num[i-1]
        
        tmp = 1
        
        for i in range(len(num) - 2, -1, -1):
            tmp *= num[i + 1]
            res[i] *= tmp
            
        res[0] = tmp
        
        return res

    
    # author: Saad & Othman & Mass
    # time O(n)
    # space O(n)
    def product_except_self_sol1(self, num: List[int]) -> List[int]:
        white = [1] * (len(num) - 1)
        yellow = [1] * (len(num) - 1)
        
        white[0] =  num[0]
        yellow[0] = num[len(num) - 1]
        
        
        for i in range(1, len(num) - 1):
            white[i] = white[i-1] * num[i]
            yellow[i] = yellow[i-1] * num[len(num) - i - 1]
            
        res = [1] * len(num)
        res[0] = yellow[len(yellow) - 1]
        res[len(res) - 1] = white[len(white) - 1]
        
        
        for i in range(1, len(res) - 1):
            res[i] = white[i-1] * yellow[len(yellow) - i - 1]
            
        return res
