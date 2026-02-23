class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:

        # checking = ''.join(words)

        # i = 0

        # # while i < len(checking):
        # #     if checking[i] == s[0]:
        # #         if not len(checking) - i >= len(s):
        # #             return False
        # #         if checking[i:i+len(s)] == s:
        # #             return True
        # #     i += 1



        return s == ''.join(words)[:len(s)] and len(s) in [len(words[i]) + sum([len(words[j]) for j in range(i)]) for i in range(len(words))]