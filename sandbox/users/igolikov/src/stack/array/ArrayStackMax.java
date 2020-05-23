package stack.array;

import java.lang.reflect.Array;
import java.util.Arrays;

@SuppressWarnings("unchecked")
public class ArrayStackMax<T extends Comparable<T>> implements MaxStack<T> {
    private static final int DEFAULT_CAPACITY = 10;
    private Container<T>[] store;
    private int length = 0;

    public ArrayStackMax(int capacity) {
        this.store = (Container<T>[]) Array.newInstance(Container.class, Math.max(capacity, DEFAULT_CAPACITY));
    }

    public synchronized void push(T val) {
        if (length == capacity()) {
            this.store = Arrays.copyOf(store, store.length * 2);
        }

        store[length] = new Container<>(val, max(val, max()));
        length++;
    }

    public synchronized T pop() {
        if (length == 0) {
            return null;
        } else {
            length--;
            Container<T> result = store[length];
            store[length] = null;
            return result.value;
        }
    }

    public T peek() {
        if (length == 0) {
            return null;
        } else {
            return store[length - 1].value;
        }
    }

    public int capacity() {
        return store.length;
    }

    public int size() {
        return length;
    }

    public T max() {
        if (length == 0) {
            return null;
        }
        return store[length - 1].max;
    }

    private T max(T a, T b) {
        if (a == null) {
            return b;
        }
        if (b == null) {
            return a;
        }
        return a.compareTo(b) >= 1 ? a : b;
    }

    private static class Container<T extends Comparable<T>> {
        private final T value;
        private T max;

        public Container(T value, T max) {
            this.value = value;
            this.max = max;
        }
    }
}
