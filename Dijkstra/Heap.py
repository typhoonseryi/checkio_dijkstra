class Heap:
    def __init__(self):
        self.data = []

    def peek(self):
        return self.data[0] if bool(self.data) else None

    def insert(self, element):
        self.data.append(element)
        curr_index = len(self.data) - 1
        parent_index = (curr_index - 1) // 2
        parent = self.data[parent_index] if len(self.data) > parent_index and parent_index >= 0 else None
        while parent and parent[0] > element[0]:
            self.data[curr_index], self.data[parent_index] = self.data[parent_index], self.data[curr_index]
            curr_index = parent_index
            parent_index = (curr_index - 1) // 2
            parent = self.data[parent_index] if len(self.data) > parent_index and parent_index >= 0 else None

    def pop(self):
        if len(self.data) == 0:
            return None
        if len(self.data) == 1:
            return self.data.pop(0)
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        res = self.data.pop()
        curr = self.data[0]
        curr_index = 0
        left_child_index = 2*curr_index+1
        right_child_index = 2*curr_index+2
        left_child = self.data[left_child_index] if left_child_index < len(self.data) else None
        right_child = self.data[right_child_index] if right_child_index < len(self.data) else None
        while (left_child or right_child) and ((left_child and left_child[0] < curr[0]) or (right_child and right_child[0] < curr[0])):
            if left_child and right_child:
                min_child = min(left_child[0], right_child[0])
                min_child_index = [d[0] for d in self.data].index(min_child)
            elif left_child:
                min_child_index = left_child_index
            else:
                min_child_index = right_child_index
            self.data[curr_index], self.data[min_child_index] = self.data[min_child_index], self.data[curr_index]
            curr_index = min_child_index
            left_child_index = 2 * curr_index + 1
            right_child_index = 2 * curr_index + 2
            left_child = self.data[left_child_index] if left_child_index < len(self.data) else None
            right_child = self.data[right_child_index] if right_child_index < len(self.data) else None
        return res

    @property
    def is_empty(self):
        return len(self.data) == 0


if __name__ == "__main__":
    h = Heap()
    h.insert((1, 3))
    h.insert((3, 3))
    h.insert((4, 3))
    h.insert((0, 3))
    h.insert((5, 3))
    h.insert((6, 3))
    print(h.data)
    print(h.peek())
    print(h.pop())
    print(h.data)
    print(h.pop())
    print(h.data)
    print(h.pop())
    print(h.data)