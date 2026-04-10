class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        res = 0
        for op in operations:
            if op == "+":
                value = records[-1] + records[-2]
                res += value
                records.append(value)
            elif op == "C":
                value = records.pop()
                res -= value
            elif op == "D":
                value = records[-1] * 2
                res += value
                records.append(value)
            else:
                value = int(op)
                res += value
                records.append(value)
        
        return res