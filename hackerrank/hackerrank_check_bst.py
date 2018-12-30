""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def get_minvalue(root):
    if root:
        if root.left:
            return get_minvalue(root.left)
    return root.data

def get_maxvalue(root):
    if root:
        if root.right:
            return get_maxvalue(root.right)
    return root.data

def check_binary_search_tree_(root,min,max):
    if root is None:
        return True
    if (root.data < min  or root.data > max):
        return False
    return check_binary_search_tree_(root.left,min,root.data) and check_binary_search_tree_(root.right,root.data,max)

