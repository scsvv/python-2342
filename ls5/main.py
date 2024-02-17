class TreeNode:
    def __init__(self, val=0, left=None, rigth=None):
        self.value = val
        self.left = left 
        self.rigth = rigth

# def tree_print(root, level=0, prefix="Root: "):
#     if root is not None:
#         print(" " * (level * 4) + prefix + str(root.value))
#         if root.left is not None or root.rigth is not None:
#             tree_print(root.left, level+1, "L----")
#             tree_print(root.rigth, level+1, "R----")

def inorderTraversal(root):
    result = []
    inorder_recursive(root, result)
    return result


def inorder_recursive(node, result):
    if node: 
        inorder_recursive(node.left, result)
        result.append(node.value)
        inorder_recursive(node.rigth, result)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.rigth = TreeNode(3)

    result = inorderTraversal(root)
    print(result)

    
