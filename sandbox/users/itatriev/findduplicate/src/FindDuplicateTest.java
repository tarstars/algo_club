import org.junit.Assert;
import org.junit.Test;

public class FindDuplicateTest {

    @Test
    public void findDuplicate() {
        final int[] testNums1 = new int[]{1, 3, 4, 2, 2};
        final int[] testNums2 = new int[]{4, 5, 3, 1, 2, 6, 5};

        Assert.assertEquals(2, FindDuplicate.findDuplicate(testNums1));
        Assert.assertEquals(5, FindDuplicate.findDuplicate(testNums2));

    }
}