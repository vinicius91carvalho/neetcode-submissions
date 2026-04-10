class MinStack:

    def __init__(self):
        self.__stack = []
        self.__min_stack = []

    def push(self, val: int) -> None:
        self.__stack.append(val)
        min_pos = self.__min_stack[-1] if len(self.__min_stack) else val
        if val > min_pos:
            val = min_pos    
        self.__min_stack.append(val)

    def pop(self) -> None:
        self.__min_stack.pop()
        self.__stack.pop()

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__min_stack[-1]
