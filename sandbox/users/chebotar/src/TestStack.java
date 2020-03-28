class TestStack {

    public static void main(String[] args) {
        testQueue1();
        testQueue2();
        testStack();

    }

    private static void testStack() {
        final Stack stack = new Stack(10);
        assertTrue(stack.size() == 0);
        stack.push(8);
        assertTrue(stack.size() == 1);
        assertTrue(stack.max() == 8);
        assertTrue(stack.peek() == 8);
        stack.push(5);
        assertTrue(stack.size() == 2);
        assertTrue(stack.max() == 8);
        stack.push(11);
        stack.push(11);
        stack.push(11);
        assertTrue(stack.max() == 11);
        assertTrue(stack.pop() == 11);
        assertTrue(stack.max() == 11);
        System.out.println("");
        System.out.println("Stack");
        System.out.println(stack);
        System.out.println("Stack max values");
        System.out.println(stack.maxValuesString());
    }

    private static void testQueue2() {
        System.out.println("");
        System.out.println("Queue2");
        final Queue queue2 = new Queue(10,1,2,3,4);
        System.out.println("Pop element: " + queue2.pop());
        queue2.push(5);
        queue2.push(6);
        queue2.push(7);
        System.out.println(queue2);
        System.out.println("Pop element: " + queue2.pop());
        System.out.println("Pop element: " + queue2.pop());
        System.out.println("Pop element: " + queue2.pop());
        System.out.println("Pop element: " + queue2.pop());
        System.out.println(queue2);
    }

    private static void testQueue1() {
        final Queue queue = new Queue(10);
        assertTrue(queue.size() == 0);
        queue.push(8);
        assertTrue(queue.size() == 1);
        assertTrue(queue.max() == 8);
        assertTrue(queue.peek() == 8);
        queue.push(5);
        assertTrue(queue.size() == 2);
        assertTrue(queue.pop() == 8);
        assertTrue(queue.max() == 5);
        queue.push(11);
        queue.push(11);
        queue.push(11);
        assertTrue(queue.max() == 11);
        assertTrue(queue.pop() == 5);
        assertTrue(queue.max() == 11);
        assertTrue(queue.pop() == 11);
        assertTrue(queue.max() == 11);
        System.out.println("");
        System.out.println("Queue");
        System.out.println(queue);
        queue.clear();
        System.out.println("Queue cleared: " + queue);
    }

    private static void assertTrue(final boolean b) {
        if (!b) {
            throw new RuntimeException("assertTrue fails");
        }
    }
}