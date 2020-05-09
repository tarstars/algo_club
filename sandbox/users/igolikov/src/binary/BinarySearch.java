package binary;

import java.util.Arrays;

import static java.util.Arrays.copyOfRange;

public class BinarySearch {
    public static int binaryIndexSearch(int[] sorted, int elem) {
        int boundIndex = sorted.length / 2;
        if (elem < sorted[0] || elem > sorted[sorted.length - 1]) {
            throw new IllegalArgumentException();
        }
        if (elem == sorted[boundIndex]) {
            return boundIndex;
        }
        if (elem > sorted[boundIndex]) {
            return boundIndex + binaryIndexSearch(copyOfRange(sorted, boundIndex, sorted.length), elem);
        } else {
            int[] newArray = Arrays.copyOfRange(sorted, 0, boundIndex);
            return boundIndex - newArray.length + binaryIndexSearch(newArray, elem);
        }
    }

    public static void main(String[] args) {
        int[] array = new int[]{-23, -4, 0, 1, 2, 5, 7, 9, 34, 123};
        int elem = 0;
        System.out.println(binaryIndexSearch(array, elem));

    }
}
