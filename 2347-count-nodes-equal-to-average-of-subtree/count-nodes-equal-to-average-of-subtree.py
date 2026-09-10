# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans = 0

        def solve(node):
            if node is None:
                return 0, 0

            left_sum, left_count = solve(node.left)
            right_sum, right_count = solve(node.right)

            total = left_sum + right_sum + node.val
            count = left_count + right_count + 1

            if node.val == total // count:
                self.ans += 1

            return total, count

        solve(root)
        return self.ans        