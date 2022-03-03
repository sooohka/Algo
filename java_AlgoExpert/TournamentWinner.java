import java.util.*;

class Program
{
	public String tournamentWinner(ArrayList<ArrayList<String>> competitions, ArrayList<Integer> results)
	{
		Map<String, Integer> dict = new HashMap<String, Integer>();

		String ans = "";
		dict.put(ans, 0);
		for (int i = 0; i < competitions.size(); i += 1)
		{
			String winner = competitions.get(i).get((results.get(i) + 1) % 2);
			update(winner, dict);
			if (dict.get(winner) > dict.get(ans))
				ans = winner;
		}
		return ans;
	}

	public void update(String winner, Map<String, Integer> dict)
	{
		if (dict.containsKey(winner))
			dict.put(winner, dict.get(winner) + 3);
		else
			dict.put(winner, 3);
	}
}

