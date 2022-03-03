
class Program {
	public static void swap(int[] array, int a, int b) {
		int temp = array[a];

		array[a] = array[b];
		array[b] = temp;
	}

	public static int[] selectionSort(int[] array) {
		int i = 0;
		int j;
		while (i < array.length) {
			j = i;
			while (j < array.length) {
				if (array[j] < array[i])
					swap(array, i, j);
				j += 1;
			}
			i += 1;
		}
		return array;
	}
}
