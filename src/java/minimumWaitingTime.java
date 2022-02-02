
// sol1
class Program
{
	public int minimumWaitingTime(int[] queries)
	{
		Arrays.sort(queries);
		int sum = 0;
		int prev = 0;
		// 1 2 2 3 6
		// 0
		// 1							1
		// 1 + 2					3
		// 1 + 2 + 2			5
		// 1 + 2 + 2 + 3	8
		for (int i = 1; i < queries.length; i += 1)
		{
			prev = 0;
			for (int j = 0; j < i; j += 1) prev += queries[j];
			sum += prev;
			System.out.println(prev + " " + sum);
		}
		return sum;
	}
}

// sol2

class Program
{
	public int minimumWaitingTime(int[] queries)
	{
		int sum = 0;
		int cur = 0;

		Arrays.sort(queries);
		for (int i = 0; i < queries.length; i += 1)
			sum += (queries.length - (i + 1)) * queries[i];
		return sum;
	}
}

