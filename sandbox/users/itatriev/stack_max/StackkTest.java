import static org.junit.Assert.assertEquals;
import java.util.function.Predicate;
import org.junit.Test;

public class StackkTest {
    @Test
    public void createStakk_00() {
        StackkTest tester = new StackkTest();

	Stackk s1 = new Stackk(10);
	Stackk s2 = new Stackk(10);

	s1.push(1);
	assertEquals(1, s1.peek());
	assertEquals(1, s1.peekMax());

    }
}

