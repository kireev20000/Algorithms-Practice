class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root):
    if root is None:
        return float('-inf')

    v0 = root.value
    v1 = solution(root.left)
    v2 = solution(root.right)

    if v1 > v0:
        v0 = v1

    if v2 > v0:
        v0 = v2
    return v0


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == "__main__":
    test()