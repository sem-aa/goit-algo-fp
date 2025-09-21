from tree_data import draw_tree
from heap_utils import build_heap_tree

# Example heap array
heap_array = [10, 15, 30, 40, 50, 100, 40]

# Build tree fom heap
root = build_heap_tree(heap_array)

# visuality
draw_tree(root)