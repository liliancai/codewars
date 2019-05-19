/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 //Runtime: 0 ms, faster than 100.00% of Java online submissions for Same Tree.

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p==null&&q==null) return true;
        if(p==null||q==null) return false;
        if(p.val!=q.val) return false;
        if(p.val==q.val) 
            return isSameTree(p.left,q.left) && isSameTree(p.right,q.right);
        return false;
    }
}
