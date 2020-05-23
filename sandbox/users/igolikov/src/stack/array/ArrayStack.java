package stack.array;

import java.lang.reflect.Array;
import java.util.Arrays;

@SuppressWarnings("unchecked")
public class ArrayStack<T> implements Stack<T> {
    private static final int DEFAULT_CAPACITY = 10;
    private T[] store;
    private int length = 0;

    public ArrayStack(int capacity, Class<T> elemType) {
        this.store = (T[]) Array.newInstance(elemType, Math.max(capacity, DEFAULT_CAPACITY));
    }

    public ArrayStack(Class<T> elemType) {
        this.store = (T[]) Array.newInstance(elemType, DEFAULT_CAPACITY);
    }

    public synchronized void push(T val) {
        if (length == capacity()) {
            this.store = Arrays.copyOf(store, store.length * 2);
        }
        store[length] = val;
        length++;
    }

    public synchronized T pop() {
        if (length == 0) {
            return null;
        } else {
            length--;
            T result = store[length];
            store[length] = null;
            return result;
        }
    }

    public T peek() {
        if (length == 0) {
            return null;
        } else {
            return store[length - 1];
        }
    }

    public int capacity() {
        return store.length;
    }

    public int size() {
        return length;
    }
}
