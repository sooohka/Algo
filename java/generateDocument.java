import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

class Program {
	public Map<Character, Integer> parseMap(String str) {
		Map<Character, Integer> map = new HashMap<>();
		for (int i = 0; i < str.length(); i += 1) {
			char c = str.charAt(i);
			if (map.containsKey(c))
				map.put(c, map.get(c) + 1);
			else
				map.put(c, 1);
		}
		return map;
	}

	public boolean generateDocument(String characters, String document) {

		Map<Character, Integer> cMap = parseMap(characters);
		Map<Character, Integer> dMap = parseMap(document);
		for (Character c : new ArrayList<>(dMap.keySet())) {
			if (!cMap.containsKey(c) || dMap.get(c) > cMap.get(c))
				return false;
		}
		return true;
	}
}
