def isBalanced(self, root):

    def dfs(root):
        if not root:
            return [True, 0] # Balanced, height 

        left = dfs(root.left)
        right = dfs(root.right)
        balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

        return [balanced, 1 + max(left[1], right[1])]