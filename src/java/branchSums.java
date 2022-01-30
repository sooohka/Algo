import java.util.*;

class Program
{
	// This is the class of the input root. Do not edit it.
	public static class BinaryTree
	{
		int        value;
		BinaryTree left;
		BinaryTree right;

		BinaryTree(int value)
		{
			this.value = value;
			this.left = null;
			this.right = null;
		}
	}

	public static List<Integer> branchSums(BinaryTree root)
	{
		List<Integer> ans = new ArrayList<>();
		int           sum = 0;
		branchSums(root, sum, ans);
		return ans;
	}

	public static void branchSums(BinaryTree root, int sum, List<Integer> ans)
	{
		if (root == null)
			return;
		sum += root.value;
		if (root.left == null && root.right == null)
		{
			ans.add(sum);
			return;
		}
		branchSums(root.left, sum, ans);
		branchSums(root.right, sum, ans);
	}
}
