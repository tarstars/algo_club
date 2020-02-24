import java.util.*;

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
			return "(" + t + ", " + p + ", " + q  + ") ";
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

	static int[][] triangleGraph() {
		return new int[][]{
				{1, 2}, // 0
				{0, 2}, // 1
				{0, 1}  // 2
		};
	}

	static int[][] drawGraph() {
		return new int[][]{
				{1, 3},
				{4, 3, 0},
				{5},
				{0, 1, 5},
				{1, 5},
				{2, 3, 4}};
	}

	public static void main(String[] vals) {
		int[][] graph = drawGraph();

		CatMouse sam = new CatMouse();
		System.out.print("output = " + sam.catMouseGame(graph));
	}

	public void dumpBackTrack(Map<Position, List<Position>> backTrack) {
		for (Map.Entry<Position, List<Position>> onePair : backTrack.entrySet()) {
			System.out.println("" + onePair);
		}
	}

	public int catMouseGame(int[][] graph) {
		// (t, p, q) = alpha
		// t - turn, -1 - cat, 1 - mouse
		// p - position of the cat, 0 is forbidden because it is a hole
		// q - position of the mouse
		int n = graph.length;
		Map<Position, List<Position>> backTrack = new HashMap<>();
		Map<Position, Integer> score = new HashMap<>();

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
}
