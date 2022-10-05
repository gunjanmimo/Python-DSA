""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""


def check_binary_search_tree_(root):
    def dfs(root, lower, upper):
        if not root:
            return True
        elif root.data < lower or root.data > upper:
            return False
        else:
            return dfs(root.left, lower, root.data - 1) and dfs(
                root.right, root.data + 1, upper
            )

    return dfs(root, 0, 10000)
