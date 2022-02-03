import java.util.*;
class Program
{
	public boolean classPhotos(ArrayList<Integer> rs, ArrayList<Integer> bs)
	{
		ArrayList<Integer> front;
		ArrayList<Integer> back;
		Collections.sort(rs);
		Collections.sort(bs);
		if (rs.get(0) == bs.get(0))
			return false;
		if (rs.get(0) > bs.get(0))
		{
			front = rs;
			back = bs;
		}
		else
		{
			front = bs;
			back = rs;
		}
		for (int i = 0; i < front.size(); i += 1)
		{
			if (back.get(i) > front.get(i))
				return false;
		}
		return true;
	}
}
