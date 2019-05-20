/*Time: O(n^2) in worst case (no branching); O(nlogn) in best case (balanced tree).*/
// DFS
//Runtime: 11 ms, faster than 58.88% of Java online submissions for Path Sum III.

public class Solution {
    public int pathSum(TreeNode root, int sum) {
        if (root == null) return 0;
        return pathSumFrom(root, sum) + pathSum(root.left, sum) + pathSum(root.right, sum);
    }
    
    private int pathSumFrom(TreeNode node, int sum) {
        if (node == null) return 0;
        return (node.val == sum ? 1 : 0) 
            + pathSumFrom(node.left, sum - node.val) + pathSumFrom(node.right, sum - node.val);
    }
}
