class MyQueue:

    def __init__(self):
        self.left_stack = []
        self.pop_number = None

    def push(self, x: int) -> None:
        self.left_stack.append(x)

    def pop(self) -> int:
        self.pop_number = self.left_stack[0]
        self.left_stack.remove(self.pop_number)    
        return self.pop_number
    def peek(self) -> int:
        return self.left_stack[0]

    def empty(self) -> bool:
        if self.left_stack == []:       #這裡將None 改為[] 直接判斷
            return True
        else: return False