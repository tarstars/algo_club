class TestStack {

    public static void main(String[] args) {
        final Stack stack = new Stack(10);
        assertTrue(stack.size() == 0);
        stack.push(8);
        assertTrue(stack.size() == 1);
        assertTrue(stack.max() == 8);
        assertTrue(stack.peek() == 8);
        assertTrue(stack.size() == 1);
        stack.push(5);
        assertTrue(stack.size() == 2);
        assertTrue(stack.max() == 8);
        stack.push(11);
        stack.push(11);
        stack.push(11);
        assertTrue(stack.max() == 11);
        assertTrue(stack.pop() == 11);
        assertTrue(stack.max() == 11);
        System.out.println(stack);
        System.out.println(stack.maxValuesString());

    }

    private static void assertTrue(final boolean b) {
        if (!b) {
            throw new RuntimeException("assertTrue fails");
        }
    }
}