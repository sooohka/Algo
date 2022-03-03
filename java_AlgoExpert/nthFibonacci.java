
// recursive
class Program {
    public static int getNthFib(int n) {
        if (n == 1)
            return 0;
        if (n == 2)
            return 1;
        return getNthFib(n - 1) + getNthFib(n - 2);
    }
}

// dp
import java.util.*;

class Program {
    public static int getNthFib(int n) {
        if (n == 1)
            return 0;
        if (n == 2)
            return 1;
        List<Integer> dp = new ArrayList<>();
        dp.add(0);
        dp.add(1);
        for (int i = 2; i < n; i += 1) {
            dp.add(dp.get(i - 2) + dp.get(i - 1));
        }
        return dp.get(n - 1);
    }
}

// best

class Program {
    public static int getNthFib(int n) {
        if (n == 1)
            return 0;
        if (n == 2)
            return 1;
        int[] last = { 0, 1 };
        int temp = 0;
        int cur = 2;
        while (cur < n - 1) {
            temp = last[0];
            last[0] = last[1];
            last[1] = temp + last[1];
            cur += 1;
            System.out.println(last[1]);
        }
        return last[0] + last[1];
    }
}
