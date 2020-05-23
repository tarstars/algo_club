public class PascalTriangleBinom {
    public static void main(String[] args) {
        for (int i =0; i < 10; i++) {
            printRowConstant(i);
        }
    }

    private static void print(int n) {
        for (int i = 0; i <= n; i++) {
            System.out.print(binom(n, i) + " ");
        }
        System.out.println();
    }

    private static int binom(int n, int k) {
        if (k == 0 || n == k) {
            return 1;
        }
        return binom(n - 1, k) + binom(n - 1, k - 1);
    }

    private static void printRowConstant(int n) {
        int r = 1;
        System.out.print(r + " ");
        for (int k = 0; k < n; ++k) {
            r = (r * (n - k) / (k + 1));
            System.out.print(r + " ");
        }
        System.out.println();
    }
}
