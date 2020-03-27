public class PascalTriangle {
    public void main(String[] argv) {
        for (int n = 0; n < 10; ++n) {
            printRow(n);
        }
    }

    private void printRow(int n) {
        for (int x = 0; x <= n; ++x) {
            System.out.println(x);
        }
    }
}
