def invertTree(root):

    if not root:
        return None

    tmp = root.left 
    root.left = root.right
    root.right = tmp

    invertTree(root.left)
    invertTree(root.right)

    return root