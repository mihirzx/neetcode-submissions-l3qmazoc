# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        def bfs(node):
            queue = deque()
            if node:
                queue.append(node)
            res = []
            while len(queue) > 0:
                level = []
                for _ in range (len(queue)):
                    curr = queue.popleft()
                    level.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                res.append(level)
            return res
        return bfs(root)
                

                
        