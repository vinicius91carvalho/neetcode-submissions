class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            mapper = {}
            for c in s:
                if c not in mapper:
                    mapper[c] = 1
                else:
                    mapper[c] += 1
            for c in t:
                if c not in mapper:
                    return False
                else:
                    mapper[c] -= 1
            for k in mapper:
                if mapper[k] != 0:
                    return False
            return True
        return False