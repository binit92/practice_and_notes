
def goodNode(root):

    def dfs(node, maxVal):
        if not node:
            return 0

        ret = 1 if node.val >=  maxVal else 0
        maxVal = max(maxVal, node.val)

        ret += dfs(node.left, maxVal)
        ret += dfs(node.right, maxVal)

        return ret

    dfs(root,root.val)