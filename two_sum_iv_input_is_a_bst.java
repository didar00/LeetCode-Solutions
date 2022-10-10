/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> orderedNums;
    public boolean findTarget(TreeNode root, int k) {
        orderedNums = new ArrayList<>();
        inorderTraversal(root);
        
        int i = 0;
        int j = orderedNums.size()-1;
        
        while (i < j)
        {
            if (orderedNums.get(i) + orderedNums.get(j) == k)
            {
                return true;
            }
            
            if (orderedNums.get(i) + orderedNums.get(j) > k)
            {
                j--;
            }
            else
            {
                i++;
            }
        
        }
        
        return false;
        
        
    }
    
    public void inorderTraversal(TreeNode root)
    {
        if (root == null) return;
        
        inorderTraversal(root.left);
        orderedNums.add(root.val);
        inorderTraversal(root.right);
    }
}