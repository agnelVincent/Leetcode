class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:

        even = sorted([nums[i] for i in range(0,len(nums),2)])
        odd = sorted([nums[i] for i in range(1,len(nums),2)],reverse = True)

        i = j =  0
        res = []

        while i < len(even) and j < len(odd):
            res.append(even[i])
            res.append(odd[j])
            i += 1
            j += 1

        res.extend(even[i:])
        res.extend(odd[j:])

        return res