package dispersion;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Dispersion {

    public static void main(final String[] args) {
        final List<Float> list = new ArrayList<>();
        list.add(1f);
        list.add(2f);
        list.add(3f);
        list.add(4.4f);
        list.add(5f);
        float dis = normalDispersion(list);
        float disIterator = dispersionFromIterator(list.iterator());
        System.out.println("From List: " + dis);
        System.out.println("From Iterator: " + disIterator);
        // Fails on small numbers
        assertTrue(Float.compare(dis, disIterator) == 0);
    }

    private static float dispersionFromIterator(final Iterator<Float> iterator) {
        float sum = 0;
        float counter = 0;
        float sumOfPowerTwo = 0;

        while (iterator.hasNext()) {
            final Float val = iterator.next();
            sum += val;
            sumOfPowerTwo += val * val;
            counter++;
        }
        float middle = new BigDecimal(Float.toString(sum))
                .divide(new BigDecimal(Float.toString(counter)))
                .floatValue();
        final BigDecimal bigDecimal = new BigDecimal(Float.toString(sumOfPowerTwo))
                .add(new BigDecimal(Float.toString(-2 * middle * sum)))
                .add(new BigDecimal(Float.toString(middle * middle * counter)));
        return bigDecimal.floatValue();
    }

    private static float normalDispersion(final List<Float> list) {
        float result = 0;
        float sum = 0;
        for (Float val : list) {
            sum += val;
        }
        float middle = sum / (float) list.size();
        for (Float val : list) {
            float diff = (val - middle);
            result += diff * diff;
        }
        return result;
    }

    private static void assertTrue(final boolean b) {
        if (!b) {
            throw new RuntimeException("assertTrue fails");
        }
    }

}
