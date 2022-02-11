
class Program {
	public static int[] insertionSort(int[] array) {
		int temp = 0;
		for (int i = 1; i < array.length; i += 1) {

			for (int j = i; j > 0; j -= 1) {
				if (array[j] < array[j - 1]) {
					temp = array[j];
					array[j] = array[j - 1];
					array[j - 1] = temp;
				}
			}

		}
		return array;
	}
}
