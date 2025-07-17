class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.head = None
        self.tail = None
        self.capacity = capacity

    def _move_to_front(self, node: Node) -> None:
        if self.head is node:
            return

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if self.tail is node:
            self.tail = node.prev

        node.next = self.head
        node.prev = None

        if self.head:
            self.head.prev = node

        self.head = node

    def get(self, key: int) -> int:
        node = self.cache.get(key)

        if not node:
            return -1

        self._move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self._move_to_front(self.cache[key])
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node

            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                self.head = self.tail = new_node

            if len(self.cache) > self.capacity:
                del self.cache[self.tail.key]
                self.tail = self.tail.prev
                if self.tail:
                    self.tail.next = None
