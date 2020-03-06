import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.Objects;
import java.util.HashMap;
import java.util.List;
import java.util.LinkedList;
import java.util.Map;

class CatMouse {
    static final class Position {
        private int t, p, q;

        public Position(int tt, int pp, int qq) {
            t = tt;
            p = pp;
            q = qq;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (!(o instanceof Position)) {
                return false;
            }

            Position position = (Position) o;
            return position.t == t &&
                    position.p == p &&
                    position.q == q;
        }

        @Override
        public int hashCode() {
            return Objects.hash(t, p, q);
        }

        public String toString() {
            return "(" + t + ", " + p + ", " + q + ") ";
        }
    }

    static final class NeiStat {
        public int[] neiVals;

        public NeiStat() {
            neiVals = new int[3];
        }
    }

    void testPosition() {
        Position pos1 = new Position(1, 2, 3);

        HashMap<Position, List<String>> hm = new HashMap<>();
        List<String> ll1 = new LinkedList<>();
        ll1.add("first");
        hm.put(pos1, ll1);

        Position pos2 = new Position(1, 2, 3);
        List<String> ll2 = hm.get(pos2);
        ll2.add("second");
        hm.put(pos2, ll2);

        System.out.println(hm);
    }

    public void dumpBackTrack(Map<Position, List<Position>> backTrack) {
        for (Map.Entry<Position, List<Position>> onePair : backTrack.entrySet()) {
            System.out.println("" + onePair);
        }
    }

    public int solve(int[][] graph) {
        // (t, p, q) = alpha
        // t - turn, -1 - cat, 1 - mouse
        // p - position of the cat, 0 is forbidden because it is a hole
        // q - position of the mouse
        int n = graph.length;
        Map<Position, List<Position>> backTrack = new HashMap<>();
        Map<Position, Integer> score = new HashMap<>();
        Map<Position, NeiStat> nei = new HashMap<>();

        for (int p = 1; p < n; ++p) {
            for (int q = 0; q < n; ++q) {
                {
                    Position alpha = new Position(-1, p, q);
                    score.put(alpha, 0);

                    for (int pp : graph[p]) {
                        if (pp != 0) {
                            Position beta = new Position(1, pp, q);
                            List<Position> affectedPositions = backTrack.get(beta);
                            if (affectedPositions == null) {
                                affectedPositions = new LinkedList<>();
                            }
                            affectedPositions.add(alpha);
                            backTrack.put(beta, affectedPositions);

                            NeiStat ns = nei.get(alpha);
                            if (ns == null) {
                                ns = new NeiStat();
                                nei.put(alpha, ns);
                            }
                            ++ns.neiVals[1];
                        }
                    }
                }

                {
                    Position alpha = new Position(1, p, q);
                    score.put(alpha, 0);

                    for (int qq : graph[q]) {
                        Position beta = new Position(-1, p, qq);
                        List<Position> affectedPositions = backTrack.get(beta);
                        if (affectedPositions == null) {
                            affectedPositions = new LinkedList<>();
                        }
                        affectedPositions.add(alpha);
                        backTrack.put(beta, affectedPositions);
                    }
                }
            }
        }

        dumpBackTrack(backTrack);

        return 0;
    }

    public static void printDotGraph(String filename, int[][] graph) throws Exception {
        BufferedWriter dst = new BufferedWriter(new FileWriter(filename));
        int n = graph.length;
        dst.write("graph G {\n");
        for (int p = 0; p < n; ++p) {
            for (int q : graph[p]) {
                if (q > p) {
                    dst.write(p + " -- " + q + "; \n");
                }
            }
        }
        dst.write(("}\n"));
        dst.close();
    }
}
