import org.junit.Assert;
import org.junit.Test;

public class PointPropertyTest {
    @Test
    public void putGet() {
        final PointProperty<String> pp = new PointProperty<>();
        pp.put(1, 1, "abc");
        pp.put(0, 2, "def");

        Assert.assertEquals("abc", pp.get(1, 1));
        Assert.assertEquals("def", pp.get(0, 2));
        Assert.assertEquals(null, pp.get(0, 0));
    }
}
