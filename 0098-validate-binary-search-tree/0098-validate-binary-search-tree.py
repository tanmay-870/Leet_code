#leetcode 98 validate bst 
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Helper function jo har node ki valid range (low, high) check karega
        def validate(node, low, high):
            # Base case: Khali node (None) hamesha valid BST hota hai
            if not node:
                return True
            
            # Agar current node ki value apni range todti hai, toh False return kardo
            if not (low < node.val < high):
                return False
            
            # Left child: low wahi rahega, par maximum limit 'node.val' ho jayegi
            # Right child: minimum limit 'node.val' ho jayegi, aur high wahi rahega
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        # Shuruat mein root ki range -infinity se +infinity hoti hai
        return validate(root, float('-inf'), float('inf'))
           
        
        