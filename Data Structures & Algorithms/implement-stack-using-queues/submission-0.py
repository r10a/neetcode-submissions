class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.queue:
            return
        num_elements = len(self.queue)
        if num_elements == 1:
            return self.queue.pop(0)
        temp_queue = []
        for _ in range(num_elements - 1):
            temp_queue.append(self.queue.pop(0))
        response = self.queue.pop(0)
        for _ in range(num_elements - 1):
            self.queue.append(temp_queue.pop(0))
        return response

    def top(self) -> int:
        if not self.queue:
            return
        num_elements = len(self.queue)
        if num_elements == 1:
            return self.queue[0]
        temp_queue = []
        for _ in range(num_elements - 1):
            temp_queue.append(self.queue.pop(0))
        response = self.queue.pop(0)
        temp_queue.append(response)
        for _ in range(num_elements):
            self.queue.append(temp_queue.pop(0))
        return response

    def empty(self) -> bool:
        return False if self.queue else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()