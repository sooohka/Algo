class Program {
	public static int[] initNumbers(int[] numbers) {
		for (int i = 0; i < numbers.length; i += 1)
			numbers[i] = Integer.MIN_VALUE;
		return numbers;
	}

	public static void shift(int[] numbers, int loc, int num) {
		for (int i = 0; i < loc; i += 1) {
			numbers[i] = numbers[i + 1];
		}
		numbers[loc] = num;
	}

	public static int[] findThreeLargestNumbers(int[] array) {
		int[] numbers = initNumbers(new int[3]);
		for (int num : array) {
			if (num >= numbers[2])
				shift(numbers, 2, num);
			else if (num >= numbers[1])
				shift(numbers, 1, num);
			else if (num >= numbers[0])
				shift(numbers, 0, num);
		}
		return numbers;
	}
}
