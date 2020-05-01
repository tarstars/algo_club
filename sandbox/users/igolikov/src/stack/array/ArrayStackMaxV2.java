package stack.array;

public class ArrayStackMaxV2<T extends Comparable<T>> implements MaxStack<T> {
    private static final int DEFAULT_CAPACITY = 10;
    private ArrayStack<T> store;
    private ArrayStack<T> max;

    public ArrayStackMaxV2(int capacity, Class<T> elemType) {
        this.store = new ArrayStack<>(capacity, elemType);
        this.max = new ArrayStack<>(elemType);
    }

    public ArrayStackMaxV2(Class<T> elemType) {
        this.store = new ArrayStack<>(DEFAULT_CAPACITY, elemType);
        this.max = new ArrayStack<>(elemType);
    }

    @Override
    public void push(T val) {
        store.push(val);
        if (val != null && (max.peek() == null || max.peek().compareTo(val) <= 0)) {
            max.push(val);
        }
    }

    @Override
    public T pop() {
        T val = store.pop();
        if (val == null) {
            return null;
        }
        if (max.size() > 0 && max.peek().compareTo(val) == 0) {
            max.pop();
        }

        return val;
    }

    @Override
    public T peek() {
        return store.peek();
    }

    @Override
    public int size() {
        return store.size();
    }

    @Override
    public int capacity() {
        return store.capacity();
    }

    @Override
    public T max() {
        return max.peek();
    }
}
