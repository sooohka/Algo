class Program {

	public static boolean isPalindrome(String str) {
		String[] strs = str.split("");
		for (int i = 0; i <= strs.length / 2; i += 1)
			if (!strs[i].equals(strs[strs.length - 1 - i]))
				return false;
		return true;
	}
}
