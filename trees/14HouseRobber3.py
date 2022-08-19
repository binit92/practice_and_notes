def rob(root):
    
    # return pair = [withRoot, withoutRoot]
    def dfs(root):
        if not root:
            return[0,0]

        leftPair = dfs(root.left)
        rightPair = dfs(root.right)

        withRoot = root.val + leftPair[1] + rightPair[1]
        withoutRoot = max(leftPair) + max(rightPair)

        return[withRoot, withoutRoot]