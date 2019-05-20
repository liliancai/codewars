/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 Runtime: 0 ms, faster than 100.00% of Java online submissions for Same Tree.

 // 1.recursion: prooder left tree, postoder right tree
class Solution {
    public boolean isSymmetric(TreeNode root) {  
        if(root==null) return true;
            return isSymetricRecur(root.left, root.right);
       
    }
    private boolean isSymetricRecur(TreeNode left, TreeNode right){
        if(left==null||right==null)
            return left == right;
        if(left.val!=right.val)
            return false;
        return isSymetricRecur(left.left,right.right) && isSymetricRecur(left.right, right.left);
    }
}

 // 2.iteraten: level order check if symmetric
