import static org.junit.Assert.assertEquals;
import java.util.function.Predicate;
import org.junit.Test;

public class Dihotom {
    @Test
    public void lowerBoundTest() {
        Dihotom tester = new Dihotom();

        int[] a;
        a = new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

        
        System.out.println();
        for (int v = 1; v < a.length; ++v) {
            int result = find(0, a.length,  lowerBound(a, v));
            assertEquals(v - 1, result);
        }
    }

    @Test
    public void upperBoundTest() {
        Dihotom tester = new Dihotom();

        int[] a;
        a = new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

        
        System.out.println();
        for (int v = 1; v < a.length; ++v) {
            int result = find(0, a.length,  upperBound(a, v));
            assertEquals(v, result);
        }
    }

    Predicate<Integer> lowerBound(int[] a, int v) {
        return ind -> a[ind] >= v;
    }

    Predicate<Integer> upperBound(int[] a, int v) {
        return ind -> a[ind] > v;
    }

    public int find(int a, int b, Predicate<Integer> p) {
        int l = a - 1;
        int r = b;

        while (l + 1 < r) {
            int m = (l + r) / 2;
            if (p.test(m)) {  
                r = m;
            } else {
                l = m;
            }
        }

        return r;
    }
}
