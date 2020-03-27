import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;


class PointPropertyTest {
    @Test
    void testSetRead() {
        PointProperty pp = new PointProperty();
        pp.set(0, 0, "Red square");
        pp.set(0, 100, "Taldom");
        pp.set(0, 100, "kimry");

        Assertions.assertEquals("Red square", pp.get(0, 0));
        Assertions.assertEquals("kimry", pp.get(0, 100));
        Assertions.assertNull(pp.get(3, 14));
    }

    @Test
    void testLongCompute() {
        PointProperty pp = new PointProperty();
        for (int x = 0; x < 10000000; ++x) {
            pp.set(x, -x*41, "test");
        }
    }
}
