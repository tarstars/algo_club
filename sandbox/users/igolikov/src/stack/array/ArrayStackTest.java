package stack.array;


import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;

class ArrayStackTest {

    @Test
    void pushTest() {
        ArrayStack<Integer> test = new ArrayStack<>(0, Integer.class);
        int initialCapacity = test.capacity();
        for (int i = 0; i < initialCapacity; i++) {
            test.push(i);
        }
        assertEquals(initialCapacity, test.size());
        test.push(123);
        assertEquals(initialCapacity * 2, test.capacity());
    }

    @Test
    void popTest() {
        ArrayStack<Integer> test = new ArrayStack<>(10, Integer.class);
        assertNull(test.pop());
        test.push(1);
        assertEquals(1, test.pop());
    }

    @Test
    void peekTest() {
        ArrayStack<Integer> test = new ArrayStack<>(10, Integer.class);
        assertNull(test.peek());
        test.push(123);
        assertEquals(123, test.peek());
        assertEquals(1, test.size());
    }

    @Test
    void capacityTest() {
        ArrayStack<Integer> testArray = new ArrayStack<>(10, Integer.class);
        assertEquals(10, testArray.capacity());
    }

    @Test
    void lengthTest() {
        ArrayStack<Integer> testArray = new ArrayStack<>(10, Integer.class);
        assertEquals(0, testArray.size());
        testArray.push(1);
        assertEquals(1, testArray.size());
        testArray.pop();
        assertEquals(0, testArray.size());
    }
}