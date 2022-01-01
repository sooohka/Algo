import java.util.*;
class Program
{
	public static int[] twoNumberSum(int[] array, int targetSum)
	{
		for (int i = 0; i < array.length - 1; i++)
		{
			for (int j = i + 1; j < array.length; j++)
			{
				if (array[i] + array[j] == targetSum)
				{
					int[] ans = {array[i], array[j]};
					return ans;
				}
			}
		}
		return new int[0];
	}
}

