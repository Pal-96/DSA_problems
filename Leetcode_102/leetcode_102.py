# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque()
        result = []
        if not root:
            return result
        dq.append([root, 0])
        result.append([root.val])
        while dq:
            rt, level = dq.popleft()
            left = rt.left
            right = rt.right
            if left or right:
                if len(result)-1<level+1:
                    result.append([])
            if left and right:
                result[level+1].append(left.val)
                result[level+1].append(right.val)
                dq.append([left, level+1])
                dq.append([right, level+1])
            elif left:
                result[level+1].append(left.val)
                dq.append([left, level+1])
            elif right:
                result[level+1].append(right.val)
                dq.append([right, level+1])
            # print(rt.val, level)
            # print(result)
        return result