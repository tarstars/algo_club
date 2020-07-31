package stack.array;

public interface MaxStack<T extends Comparable<T>> extends Stack<T> {
    T max();
}
