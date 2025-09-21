from collections import deque
import colorsys


def generate_colors(n):
    """Generate n colors from dark to light (in hex format)."""
    colors = []
    for i in range(n):
        # change brightness from 0.3 to 1.0
        brightness = 0.3 + (0.7 * i / (n - 1 if n > 1 else 1))
        r, g, b = colorsys.hsv_to_rgb(0.58, 0.85, brightness)  # blue shade (#1296F0)
        colors.append('#{:02x}{:02x}{:02x}'.format(int(r * 255), int(g * 255), int(b * 255)))
    return colors


def bfs(root):
    """Breadth-first search (BFS) with node coloring."""
    if not root:
        return

    queue = deque([root])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    # color nodes
    colors = generate_colors(len(order))
    for i, node in enumerate(order):
        node.color = colors[i]


def dfs(root):
    """Depth-first search (DFS) with node coloring."""
    if not root:
        return

    stack = [root]
    order = []
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)

            # important: right first, then left, so left is processed first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    # color nodes
    colors = generate_colors(len(order))
    for i, node in enumerate(order):
        node.color = colors[i]

