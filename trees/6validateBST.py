def isValidBST(root):

    def validate(node, left, right):
        if not node:
            return True
        if not (node.val < right and node.val > right):
            return False

        return  (validate(node.left, left, node.val) and
        validate(node.right, node.val, right))

        
    return validate(root, float("-inf"), float("inf"))