
class Program {

	public static int binarySearch(int[] array, int target) {
		return binarySearch(array, target, 0, array.length - 1);
	}

	public static int binarySearch(int[] array, int target, int left, int right) {
		if (left > right)
			return -1;
		int middle = (left + right) / 2;
		if (array[middle] == target)
			return middle;
		if (array[middle] > target)
			return binarySearch(array, target, left, middle - 1);
		if (array[middle] < target)
			return binarySearch(array, target, middle + 1, right);
		return -1;
	}
}
