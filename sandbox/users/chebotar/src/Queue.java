class Queue {

    final Stack income;
    final Stack outcome;

    public Queue(final int minimalMaxRangeSize) {
        outcome = new Stack(minimalMaxRangeSize);
        income = new Stack(minimalMaxRangeSize);
    }

    public Queue(final int minimalMaxRangeSize, final int... values) {
        outcome = new Stack(minimalMaxRangeSize);
        income = new Stack(minimalMaxRangeSize, values);
    }

    public int size() {
        return income.size() + outcome.size();
    }

    public int peek() {
        if (outcome.size() == 0) {
            moveAllIncome();
        }
        return outcome.peek();
    }

    private void moveAllIncome() {
        while (income.size() != 0) {
            outcome.push(income.pop());
        }
    }

    public void push(int i) {
        income.push(i);
    }


    public int pop() {
        if (outcome.size() == 0) {
            moveAllIncome();
        }
        return outcome.pop();
    }

    public int max() {
        if (size() == 0) {
            throw new RuntimeException("no elements");
        }

        if (income.size() == 0) {
            return outcome.max();
        }

        if (outcome.size() == 0) {
            return income.max();
        }

        return Math.max(income.max(), outcome.max());
    }

    @Override
    public String toString() {
        return income.toString() + outcome.toString();
    }

    public void clear() {
        income.clear();
        outcome.clear();
    }
}