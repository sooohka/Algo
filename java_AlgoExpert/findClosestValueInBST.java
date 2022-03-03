
// non-recursive
import java.util.*;

class Program
{
	public static int findClosestValueInBst(BST tree, int target)
	{
		int currentValue = tree.value;
		while (tree != null)
		{
			if (currentValue == target)
				return currentValue;
			else if (tree.value < target)
				tree = tree.right;
			else if (tree.value > target)
				tree = tree.left;

			if (tree == null)
				return currentValue;

			if (Math.abs(target - tree.value) < Math.abs(target - currentValue))
			{
				currentValue = tree.value;
			}
		}
		return currentValue;
	}

	static class BST
	{
		public int value;
		public BST left;
		public BST right;

		public BST(int value)
		{
			this.value = value;
		}
	}
}

// recursive
class Program
{
	public static int findClosestValueInBst(BST tree, int target)
	{
		return f(tree, target, tree.value);
	}

	public static int f(BST tree, int target, int prev)
	{
		if (tree == null)
			return prev;
		if (Math.abs(target - tree.value) < Math.abs(target - prev))
		{
			prev = tree.value;
		}
		if (target > tree.value)
			return f(tree.right, target, prev);
		else if (target < tree.value)
			return f(tree.left, target, prev);
		return tree.value;
	}

	static class BST
	{
		public int value;
		public BST left;
		public BST right;

		public BST(int value)
		{
			this.value = value;
		}
	}
}

