class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:

        return s == ''.join(words)[:len(s)] and len(s) in [len(words[i]) + sum([len(words[j]) for j in range(i)]) for i in range(len(words))]