import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestFactory;


public class CatMouseTest {

    CatMouse catMouse = new CatMouse();

    @TestFactory
    int[][] triangleGraph() {
        return new int[][]{
                {1, 2}, // 0
                {0, 2}, // 1
                {0, 1}  // 2
        };
    }

    @TestFactory
    int[][] drawGraph() {
        return new int[][]{
                {1, 3},
                {4, 3, 0},
                {5},
                {0, 1, 5},
                {1, 5},
                {2, 3, 4}};
    }

    @Test
    void testTriangleMaze() {
        catMouse.solve(triangleGraph());
    }

    @Test
    void testDrawMaze() {
        catMouse.solve(drawGraph());
    }

    @Test
    void printMazeGraph() throws Exception {
        CatMouse.printDotGraph("drawMaze.dot", drawGraph());
    }
}
