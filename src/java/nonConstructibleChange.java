import java.util.*;

class Program
{
	public int sumList(List<Integer> list)
	{
		int sum = 0;
		for (int i = 0; i < list.size(); i += 1)
		{
			sum += list.get(i);
		}
		return sum;
	}

	public void dfs(List<Integer> list, List<Boolean> visited, List<Integer> temp, int cur, List<Integer> ans)
	{
		int sum = sumList(temp);
		if (!ans.contains(sum))
			ans.add(sum);
		for (int i = cur; i < list.size(); i += 1)
		{
			if (visited.get(i))
				continue;
			visited.set(i, true);
			temp.add(list.get(i));
			dfs(list, visited, temp, i, ans);
			temp.remove(temp.size() - 1);
			visited.set(i, false);
		}
	}

	public int nonConstructibleChange(int[] coins)
	{
		if (coins.length == 0)
			return 1;

		List<Integer> list = new ArrayList<>();
		List<Boolean> visited = new ArrayList<>();
		List<Inteer>  temp = new ArrayList<>();
		List<Integer> ans = new ArrayList<>();
		for (int i : coins)
		{
			list.add(i);
			visited.add(false);
		}

		dfs(list, visited, temp, 0, ans);
		Collections.sort(ans);
		System.out.println(ans);
		for (int i = 1; i < ans.size(); i += 1)
		{
			if (ans.get(i - 1) + 1 == ans.get(i))
				continue;
			return ans.get(i - 1) + 1;
		}
		return ans.get(ans.size() - 1) + 1;
	}
}

// OPTIMAL SOLUTION
/* class Program */
/* { */
/*     public int nonConstructibleChange(int[] coins) */
/*     { */
/*         Arrays.sort(coins); */
/*         int coinSum = 0; */
/*         for (int coin : coins) */
/*         { */
/*             if (coin > coinSum + 1) */
/*                 return coinSum + 1; */
/*             coinSum += coin; */
/*         } */
/*         return coinSum + 1; */
/*     } */
/* } */
