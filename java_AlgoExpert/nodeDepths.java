import java.util.*;
// sol 1
class Program
{
	public static int sum(List<Integer> list)
	{
		int sum = 0;
		for (int v : list) sum += v;
		return sum;
	}
	public static int nodeDepths(BinaryTree root)
	{
		List<Integer> ans = new ArrayList<>();
		nD(root, 0, ans);
		return sum(ans);
	}
	public static void nD(BinaryTree root, int depth, List<Integer> ans)
	{
		if (root == null)
			return;
		ans.add(depth);
		depth += 1;
		nD(root.left, depth, ans);
		nD(root.right, depth, ans);
	}
	static class BinaryTree
	{
		int        value;
		BinaryTree left;
		BinaryTree right;
		public BinaryTree(int value)
		{
			this.value = value;
			left = null;
			right = null;
		}
	}
}
// sol2

class Program
{
	public static int nodeDepths(BinaryTree root)
	{
		List<Level> stack = new ArrayList<Level>();
		int         sum = 0;
		stack.add(new Level(root, 0));
		while (stack.size() > 0)
		{
			Level      lv = stack.remove(stack.size() - 1);
			BinaryTree node = lv.node;
			int        depth = lv.depth;

			if (node == null)
				continue;
			sum += depth;
			stack.add(new Level(node.left, depth + 1));
			stack.add(new Level(node.right, depth + 1));
		}
		return sum;
	}

	static class Level
	{
		BinaryTree node;
		int        depth;

		Level(BinaryTree bt, int depth)
		{
			this.node = bt;
			this.depth = depth;
		}
	}

	static class BinaryTree
	{
		int        value;
		BinaryTree left;
		BinaryTree right;

		public BinaryTree(int value)
		{
			this.value = value;
			left = null;
			right = null;
		}
	}
}

