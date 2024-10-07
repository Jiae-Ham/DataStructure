class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity-1

    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = item
        else: pass

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else: pass

    def __str__(self):
        return str(self.array[0:self.top+1][::-1])

    def size(self): return self.top+1

if __name__ == "__main__":
    s = ArrayStack(10)
    for i in range(1,6):		# i = 1, 2, 3, 4, 5
        s.push(i)			    # push 연산 5회
    print(' push 5회: ', s)	        # 스택 내용 출력
    print(' push 5회: ', s.array)	# 스택 내용 출력