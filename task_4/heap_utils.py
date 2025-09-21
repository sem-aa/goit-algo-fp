from tree_data import Node

def build_heap_tree(heap):
    """Будує бінарне дерево з масиву (представлення бінарної купи)"""
    nodes = [Node(val) for val in heap]

    for i in range(len(heap)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(heap):
            nodes[i].left = nodes[left_index]
        if right_index < len(heap):
            nodes[i].right = nodes[right_index]

    return nodes[0] if nodes else None