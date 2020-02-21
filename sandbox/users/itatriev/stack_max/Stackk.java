import java.lang.Math;

public class Stackk {
    
    private int[] arr;
    private int[] maxArr;
    private int head;
    private int maxSize;
    private int size;

    public Stackk(final int maxSize) {
        this.maxSize = maxSize;
        arr = new int[maxSize];
        maxArr = new int[maxSize];
	head = -1;
	size = 0;
    }

    public void push(final int num) {
        if (size >= maxSize) return;
        arr[++head] = num;
        maxArr[head] = (head == 0) ? num : Math.max(num, maxArr[head-1]);
        size++;
    }

    public int pop() {
        return arr[head--];
    }

    public int peekMax() {
        return maxArr[head];
    }

    public int peek() {
	return arr[head];
    }

    public int size() {
        return size;
    }
}
