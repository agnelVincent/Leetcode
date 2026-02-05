class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        for ind1, val1 in enumerate(arr1):
            flag = False
            for ind2, val2 in enumerate(arr2):
                if abs(val1-val2) <= d:
                    flag = True
                    break
            if not flag:
                res += 1
        
        return res
