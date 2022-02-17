import java.util.HashMap;

class Program {
	public HashMap<Character, Integer> parse(String string) {
		HashMap<Character, Integer> map = new HashMap<>();
		for (int i = 0; i < string.length(); i += 1) {
			char c = string.charAt(i);
			if (map.containsKey(c))
				map.put(c, map.get(c) + 1);
			else
				map.put(c, 1);
		}
		return map;
	}

	public int firstNonRepeatingCharacter(String string) {
		HashMap<Character, Integer> map = new HashMap<>();
		map = parse(string);
		for (int i = 0; i < string.length(); i += 1) {
			char c = string.charAt(i);
			if (map.get(c) == 1)
				return i;
		}
		return -1;
	}
}
