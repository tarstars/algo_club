import java.util.Map;
import java.util.HashMap;

public class PointProperty<T> {

    private final Map<Point, T> propertiesMap = new HashMap<>();

    public PointProperty() {

    }

    public void put(final int x, final int y, final T value) {
        propertiesMap.put(new Point(x, y), value);
    }

    // returns null if:
    //      1. key does not exist 
    //      2. null value is stored under (x, y) key
    public T get(final int x, final int y) {
        return propertiesMap.get(new Point(x, y));
    }

    private static final class Point {
        private final int x;
        private final int y;

        public Point(final int x, final int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int hashCode() {
            int result = x;
            result = 31 * result + y;
            return result;
        }

        @Override
        public boolean equals(Object o) {
            if (o == null) {
                return false;
            }
            if (!(o instanceof Point)) {
                return false;
            }
            return (x == ((Point) o).x && y == ((Point) o).y);
        }
    }
}