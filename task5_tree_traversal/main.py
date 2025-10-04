from tree_traversal import Node, dfs_traversal, bfs_traversal, draw_tree

def main():
    # Створюємо дерево
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    print("DFS Traversal")
    visited_dfs = dfs_traversal(root)
    draw_tree(root, visited_dfs)

    print("BFS Traversal")
    visited_bfs = bfs_traversal(root)
    draw_tree(root, visited_bfs)

if __name__ == "__main__":
    main()