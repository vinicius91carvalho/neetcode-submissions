class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {
            "[": "]",
            "(": ")",
            "{": "}"
        }
        arr = []
        for i in range(len(s)):
            last_open_char = 0
            if len(arr) > 0:
                last_open_char = arr[len(arr) - 1]

            if  brackets_map.get(s[i], 0):
                arr.append(s[i])
            elif brackets_map.get(last_open_char) == s[i]:
                arr.pop()
            else:
                return False

        if len(arr) > 0: 
            return False 
    
        return True
