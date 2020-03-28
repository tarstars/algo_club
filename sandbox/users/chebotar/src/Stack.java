class Stack {

    private final int[] array;
    private final int[] arrayMax;
    private int pushIndex = 0;
    private int pushIndexMax = 0;

    public Stack(final int maxSize) {
        array = new int[maxSize];
        arrayMax = new int[maxSize];
    }

    public Stack(final int maxSize, final int... values) {
        array = new int[maxSize];
        arrayMax = new int[maxSize];
        for (int value : values) {
            push(value);
        }
    }

    public int size() {
        return pushIndex;
    }

    public int peek() {
        if (pushIndex <= 0) {
            throw new RuntimeException("no elements");
        }
        return array[pushIndex - 1];
    }

    public void push(int i) {
        if (pushIndex == array.length) {
            throw new RuntimeException("stack overflow =)");
        }
        array[pushIndex] = i;
        if (pushIndexMax == 0 || max() <= i) {
            pushMax(i);
        }
        pushIndex++;
    }


    public int pop() {
        final int element = peek();
        pushIndex--;
        if (max() == element) {
            popMax();
        }
        return element;
    }

    private void pushMax(int i) {
        if (pushIndexMax == arrayMax.length) {
            throw new RuntimeException("stack overflow =)");
        }
        arrayMax[pushIndexMax] = i;
        pushIndexMax++;
    }

    private void popMax() {
        pushIndexMax--;
    }

    public int max() {
        if (pushIndexMax <= 0) {
            throw new RuntimeException("no elements");
        }
        return arrayMax[pushIndexMax - 1];
    }

    @Override
    public String toString() {
        return partiallyToString(array, pushIndex);
    }

    public String maxValuesString() {
        return partiallyToString(arrayMax, pushIndexMax);
    }

    private String partiallyToString(int[] a, int index) {
        if (a == null)
            return "null";
        if (index == 0)
            return "[]";
        final StringBuilder builder = new StringBuilder()
                .append('[')
                .append(a[0]);
        for (int i = 1; i < index; i++) {
            builder.append(", ")
                    .append(a[i]);
        }
        return builder.append(']').toString();
    }

    public void clear() {
        pushIndex = 0;
        pushIndexMax = 0;
    }
}