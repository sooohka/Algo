import java.util.*;

class Program
{
	public static boolean isValidSubsequence(List<Integer> array, List<Integer> sequence)
	{
		int j = 0;
		for (int i = 0; i < array.size(); i++)
		{
			if (array.get(i) == sequence.get(j))
			{
				j++;
			}
			if (j == sequence.size())
				return true;
		}
		if (j == sequence.size())
			return true;
		return false;
	}
}

