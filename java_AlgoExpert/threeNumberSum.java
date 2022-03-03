import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Program {
	public static List<Integer[]> threeNumberSum(int[] array, int targetSum) {
		List<Integer[]> answer = new ArrayList<Integer[]>();
		Arrays.sort(array);
		for (int i = 0; i < array.length; i += 1) {
			int sub = targetSum - array[i];
			for (int j = i + 1; j < array.length; j += 1) {
				int k = array.length - 1;
				while (j < k && array[j] + array[k] >= sub) {
					if (array[j] + array[k] == sub) {
						answer.add(new Integer[] { array[i], array[j], array[k] });
					}
					k -= 1;
				}
			}
		}
		return answer;
	}
}

class Program2 {
	public static List<Integer[]> threeNumberSum(int[] array, int targetSum) {
		List<Integer[]> answer = new ArrayList<Integer[]>();
		Arrays.sort(array);
		for (int i = 0; i < array.length - 2; i += 1) {
			int sub = targetSum - array[i];
			int left = i + 1;
			int right = array.length - 1;
			while (left < right) {
				int sum = array[left] + array[right];
				if (sum == sub) {
					answer.add(new Integer[] { array[i], array[left], array[right] });
					left += 1;
					right -= 1;
				}
				if (sum < sub) {
					left += 1;
				} else if (sum > sub) {
					right -= 1;
				}
			}
		}
		return answer;
	}
}
