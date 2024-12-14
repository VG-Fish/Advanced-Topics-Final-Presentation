from typing import Self


class Node:
    def __init__(self: Self, value: int, next: "Node" = None) -> None:
        self.value = value
        self._next = next

    def __str__(self: Self) -> str:
        return f"Node({self.value})"


class Queue:
    def __init__(self: Self, node: "Node" = None) -> None:
        self.first: "Node" = node
        self.last: "Node" = node
        self.add(node)

    def add(self: Self, node: "Node") -> None:
        if node is None:
            return
        if not isinstance(node, Node):
            raise ValueError(
                "You passed in the wrong type for node, it should be an object of Node."
            )
        elif self.first is None:
            self.first = node
            self.last = node
            return

        prev: "Node" = self.last
        self.last = node
        prev._next = node

    def pop(self: Self) -> "Node":
        if self.first is None:
            return

        first: "Node" = self.first
        self.first = first._next
        return first

    def __str__(self: Self) -> str:
        current = self.first
        nodes = []
        while current:
            nodes.append(str(current))
            current = current._next
        return f"Queue([{' -> '.join(nodes)}])"


q = Queue()
q.add(Node(1))
q.add(Node(2))
print(q)

q.pop()
print(q)

q.add(Node(3))
print(q)

q.pop()
q.pop()
q.add(Node(4))
print(q)
