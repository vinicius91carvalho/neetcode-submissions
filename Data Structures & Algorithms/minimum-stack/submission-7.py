class MinStack:

    def __init__(self):
        self.__stack = []
        self.__min_value = 0

    def push(self, val: int) -> None:
        self.__stack.append(val)
        if val < self.__min_value or len(self.__stack) == 1:
            self.__min_value = val

    def pop(self) -> None:
        self.__min_value = self.__stack[0]
        self.__stack.pop()
        for i in range(len(self.__stack)):
            if self.__stack[i] < self.__min_value:
                self.__min_value = self.__stack[i]

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__min_value
