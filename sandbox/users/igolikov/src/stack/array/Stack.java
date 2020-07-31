package stack.array;

public interface Stack<T> {
    void push(T val);
    T pop();
    T peek();
    int size();
    int capacity();
}
