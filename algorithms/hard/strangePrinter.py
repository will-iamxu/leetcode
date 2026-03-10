class Solution:
    def strangePrinter(self, s: str) -> int:
        s = [c for c, _ in groupby(s)]

        @cache
        def print(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            best = 1 + print(i + 1, j)

            for k in range(i+1, j+1):
                if s[i] == s[k]:
                    best = min(best, print(i+1, k) + print(k+1,j))
            return best

        return print(0, len(s)-1) 