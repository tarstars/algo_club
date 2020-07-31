package stack.array;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ArrayStackMaxTest {

    @Test
    void max() {
        ArrayStackMax<Integer> test = new ArrayStackMax<>(0);
        assertNull(test.max());
        test.push(1);
        assertEquals(1, test.max());
        test.push(10);
        test.push(25);
        assertEquals(25, test.max());
        test.pop();
        assertEquals(10, test.max());
    }
}