import java.util.*;

class Program {
	// Tip: You can use `element instanceof ArrayList` to check whether an item
	// is an array or an integer.

	public static int productSum(ArrayList<Object> array, int multiplier) {
		int answer = 0;
		for (int i = 0; i < array.size(); i += 1) {
			Object obj = array.get(i);
			if (obj instanceof ArrayList)
				answer += productSum((ArrayList<Object>) obj, multiplier + 1);
			else
				answer += (int) obj;
		}
		return answer * multiplier;
	}

	public static int productSum(List<Object> array) {
		ArrayList<Object> list = new ArrayList<>();
		list.addAll(array);
		return productSum(list, 1);
	}
}
