class Solution:
    def isSameAfterReversals(self, num: int) -> bool:

        if num < 10 and num >= 0:
            return True

        return False if num % 10 == 0 else True