
def diameterOfBinaryTree(root):

    res = [0]

    def dfs(root):
        if not root:
            return -1

        left = dfs(root.left)
        right = dfs(root.right)

        diameter = 2 + left + right
        res[0] = max(res[0], diameter)

        return 1+  max(left, right)

    return res[0]