package stack.array;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ArrayStackMaxV2Test {

    @Test
    void arrayStackV2Test() {
        ArrayStackMaxV2<Integer> stack = new ArrayStackMaxV2<>(Integer.class);
        stack.push(10);
        assertEquals(10, stack.max());
        stack.push(40);
        assertEquals(40, stack.max());
        stack.push(40);
        stack.pop();
        assertEquals(40, stack.max());
        stack.pop();
        assertEquals(10, stack.max());
    }
}