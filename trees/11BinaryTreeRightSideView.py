def rightSideView(root):

    res = []
    q = collections.deque([root])

    while q:
        rightSide = None
        qLen = len(q)
        for i in range(qLen):
            node = q.popleft()
            if node :
                rightSide = node
                q.append(node.left)
                q.append(node.right)

        res.append(rightSide)

    return res

    