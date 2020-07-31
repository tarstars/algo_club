package binary;

public class BinarySearch {
    public static int binaryIndexSearch(int[] sorted, int elem) {
        return binaryIndexSearch(new IntSlice(sorted), elem);
    }

    public static int binaryIndexSearch(IntSlice sorted, int elem) {
        int boundIndex = (sorted.length() / 2) + sorted.getStartIndex();
        if (elem < sorted.get(sorted.getStartIndex()) || elem > sorted.get(sorted.getEndIndex())) {
            throw new IllegalArgumentException();
        }
        if (elem == sorted.get(boundIndex)) {
            return boundIndex;
        }

        if (elem > sorted.get(boundIndex)) {
            sorted.setIndices(boundIndex, sorted.getEndIndex());
        } else {
            sorted.setIndices(sorted.getStartIndex(), boundIndex - 1);
        }

        return binaryIndexSearch(sorted, elem);
    }

    public static void main(String[] args) {
        int[] array = new int[]{-23, -4, 0, 1, 2, 5, 7, 9, 34, 123};
        for (int elem : array) {
            System.out.println(binaryIndexSearch(array, elem));
        }

        int elem = -50;
        try {
            binaryIndexSearch(array, elem);
        } catch (IllegalArgumentException ex) {
            System.out.printf("Illegal argument %d", elem);
        }
    }

    public static class IntSlice {
        private int[] arr;
        private int startIndex;
        private int endIndex;

        public IntSlice(int[] arr) {
            this.arr = arr;
            this.startIndex = 0;
            this.endIndex = arr.length - 1;
        }

        public void setIndices(int startIndex, int endIndex) {
            this.startIndex = startIndex;
            this.endIndex = endIndex;
        }

        public int length() {
            return endIndex - startIndex + 1;
        }

        public int get(int index) {
            return arr[index];
        }

        public int getStartIndex() {
            return startIndex;
        }

        public int getEndIndex() {
            return endIndex;
        }
    }
}
