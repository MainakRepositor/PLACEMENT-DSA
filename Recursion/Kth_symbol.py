class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k-1).count('1') % 2