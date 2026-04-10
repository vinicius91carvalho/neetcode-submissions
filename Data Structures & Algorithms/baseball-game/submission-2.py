class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        res = 0
        for op in operations:
            if op == "+":
                res += records[-1] + records[-2]
                records.append(records[-1] + records[-2])
            elif op == "C":
                res -= records.pop()
            elif op == "D":
                res += records[-1] * 2
                records.append(records[-1] * 2)
            else:
                res += int(op)
                records.append(int(op))
        
        return res