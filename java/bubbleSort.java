
//my
class Program {
	public static int[] bubbleSort(int[] array) {
		int temp = 0;
		for (int i = 0; i < array.length; i += 1) {
			for (int j = 0; j < array.length - 1; j += 1) {
				if (array[j] > array[j + 1]) {
					temp = array[j];
					array[j] = array[j + 1];
					array[j + 1] = temp;
				}
			}
		}
		return array;
	}
}

// optimal
class Program {
	public static int[] bubbleSort(int[] array) {
		boolean swaped = false;
		int temp = 0;
		for (int i = 0; i < array.length; i += 1) {
			for (int j = 0; j < array.length - 1; j += 1) {
				if (array[j] > array[j + 1]) {
					temp = array[j];
					array[j] = array[j + 1];
					array[j + 1] = temp;
					swaped = true;
				}
			}
			if (!swaped)
				return array;
		}
		return array;
	}
}
