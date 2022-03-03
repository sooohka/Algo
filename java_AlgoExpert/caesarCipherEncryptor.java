class Program {
	public static String caesarCypherEncryptor(String str, int key) {
		int alpha = 26;
		int zAscii = 122;
		String ans = "";
		char[] chars = str.toCharArray();
		for (int i = 0; i < chars.length; i += 1) {
			int realKey = key % alpha;
			char c = (char) (chars[i] + realKey);
			if (c > zAscii)
				ans += (char) (c - alpha);
			else
				ans += (char) (c);
		}

		return ans;
	}
}
