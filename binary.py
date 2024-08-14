# Define a Node class to represent each node in the binary tree
class Node:
    def __init__(self, key):
        self.left = None  # Left child
        self.right = None  # Right child
        self.value = key  # Node value

# Insert a new node into the binary tree
def insert(root, key):
    # If the tree is empty, return a new node
    if root is None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    # Return the (unchanged) root node
    return root

# In-order traversal: Left -> Root -> Right
def inorder_traversal(root):
    if root:
        # Traverse the left subtree
        inorder_traversal(root.left)
        # Visit the root node
        print(root.value, end=' ')
        # Traverse the right subtree
        inorder_traversal(root.right)

# Pre-order traversal: Root -> Left -> Right
def preorder_traversal(root):
    if root:
        # Visit the root node
        print(root.value, end=' ')
        # Traverse the left subtree
        preorder_traversal(root.left)
        # Traverse the right subtree
        preorder_traversal(root.right)

# Post-order traversal: Left -> Right -> Root
def postorder_traversal(root):
    if root:
        # Traverse the left subtree
        postorder_traversal(root.left)
        # Traverse the right subtree
        postorder_traversal(root.right)
        # Visit the root node
        print(root.value, end=' ')

# Search for a node with a given key in the binary tree
def search(root, key):
    # Base case: root is null or key is present at root
    if root is None or root.value == key:
        return root

    # Key is greater than root's key, search in the right subtree
    if key > root.value:
        return search(root.right, key)

    # Key is smaller than root's key, search in the left subtree
    return search(root.left, key)
