# https://leetcode.com/problems/lru-cache/description/
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache(object):
    def __init__(self, capacity):
        self.cache = {}
        self.cap = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertHead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.deleteNode(node)
            self.insertHead(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self.deleteNode(node)
            newNode = Node(key, value)
            self.cache[key] = newNode
            self.insertHead(newNode)
        else:
            if len(self.cache) >= self.cap:
                lastElem = self.tail.prev
                self.deleteNode(lastElem)
                del self.cache[lastElem.key]

            newNode = Node(key, value)
            self.cache[key] = newNode
            self.insertHead(newNode)
