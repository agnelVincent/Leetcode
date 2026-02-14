class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

        def list_to_set(arr):
            return list(dict.fromkeys(arr))

        checking = list_to_set(nums1) + list_to_set(nums2) + list_to_set(nums3)
        return list(dict.fromkeys([i for i in checking if checking.count(i) >= 2]))


