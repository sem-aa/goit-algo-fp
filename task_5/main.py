from task_4.tree_data import Node, draw_tree
from task_5.traversal import bfs, dfs

# ==== Example tree ====
root = Node(10)
root.left = Node(6)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(8)
root.right.left = Node(12)
root.right.right = Node(18)

# ==== Test BFS ====
bfs(root)
print("BFS")
draw_tree(root)

# ==== Test DFS ====
dfs(root)
print("DFS")
draw_tree(root)