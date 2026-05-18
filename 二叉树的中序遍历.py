from idlelib.tree import TreeNode
from typing import Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

       def dfs(node: Optional[TreeNode]) -> None:
           if node is None:
               return
           dfs(node.left)
           ans.append(node.val)
           dfs(node.right)

       ans = []
       dfs(root)
       return ans