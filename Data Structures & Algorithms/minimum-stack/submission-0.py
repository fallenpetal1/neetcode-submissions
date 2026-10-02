class MinStack:

    def __init__(self):
        self.st = []
        self.minst = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.minst:
            mini = min(self.minst[-1], val)
        else:
            mini = val
        self.minst.append(mini)

    def pop(self) -> None:
        self.minst.pop()
        return self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minst[-1]
        