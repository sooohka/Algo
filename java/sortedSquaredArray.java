import java.util.*;

class Program
{
	static int makeItDoule(int num)
	{
		return num * num;
	}

	public int[] sortedSquaredArray(int[] array)
	{
		int[] nums = new int[array.length];
		for (int i = 0; i < nums.length; i++)
		{
			nums[i] = array[i] * array[i];
		}
		Arrays.sort(nums);
		return (nums);
	}
}

