class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def search_tree(node):
    if node is None:
        return True, None, None

    search_tree_l, min_l, max_l = search_tree(node.left)
    search_tree_r, min_r, max_r = search_tree(node.right)

    is_bst_node = (search_tree_l and search_tree_r and
                   (max_l is None or node.value > max_l) and
                   (min_r is None or node.value < min_r))

    min_value = min([x for x in [min_l, node.value, min_r] if x is not None])
    max_value = max([x for x in [max_l, node.value, max_r] if x is not None])

    return is_bst_node, min_value, max_value


def solution(root) -> bool:
    return search_tree(root)[0]


def test():
    root1 = Node(1, None, None)
    root2 = Node(4, None, None)
    root3 = Node(3, root1, root2)
    root4 = Node(8, None, None)
    root5 = Node(5, root3, root4)

    assert solution(root5)
    root2.value = 5
    assert not solution(root5)


if __name__ == "__main__":
    test()