
class Program {
	public String parse(char c, int count) {
		String ans = "";

		if (count < 10)
			ans += count + Character.toString(c);
		else {
			for (int i = 1; i <= count / 9; i += 1)
				ans += 9 + Character.toString(c);
			if (count % 9 != 0)
				ans += count % 9 + Character.toString(c);
		}
		return ans;

	}

	public String runLengthEncoding(String string) {
		String ans = "";
		char head = string.charAt(0);
		char cur;
		int count = 1;

		for (int i = 1; i < string.length(); i += 1) {
			cur = string.charAt(i);
			if (cur != head) {
				ans += parse(head, count);
				count = 0;
				head = cur;
			}
			count += 1;
		}
		ans += parse(head, count);
		return ans;
	}
}
