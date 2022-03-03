// mysolution
import java.util.*;
// faster rider determins bike speed
// red blue pair
// find fastest slowest
class Program
{
	public int tandemBicycle(int[] rs, int[] bs, boolean fastest)
	{
		int sum = 0;

		Arrays.sort(rs); // 2 3 5 5 9
		Arrays.sort(bs); // 1 2 3 6 7
		if (fastest)
			return fastest(rs, bs, rs.length - 1, rs.length - 1);
		for (int i = 0; i < rs.length; i += 1)
		{
			if (rs[i] > bs[i])
				sum += rs[i];
			else
				sum += bs[i];
		}
		return sum;
	}

	public int fastest(int[] rs, int[] bs, int rsIdx, int bsIdx)
	{
		int ans = 0;
		for (int i = 0; i < rs.length; i += 1)
		{
			if (rs[rsIdx] > bs[bsIdx])
				ans += rs[rsIdx--];
			else
				ans += bs[bsIdx--];
		}
		return ans;
	}
}

// best solution

class Program
{
	public int tandemBicycle(int[] rs, int[] bs, boolean fastest)
	{
		Arrays.sort(rs);
		Arrays.sort(bs);
		int sum = 0;

		if (fastest)
			reverseSortedArr(bs);
		for (int i = 0; i < rs.length; i += 1)
		{
			if (rs[i] > bs[i])
				sum += rs[i];
			else
				sum += bs[i];
		}
		return sum;
	}
	public void reverseSortedArr(int[] arr)
	{
		int temp;
		for (int i = 0; i < arr.length / 2; i++)
		{
			temp = arr[arr.length - i - 1];
			arr[arr.length - i - 1] = arr[i];
			arr[i] = temp;
		}
	}
}

