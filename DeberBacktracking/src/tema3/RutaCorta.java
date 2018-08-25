package tema3;

public class RutaCorta {

    private int M, N;
    private int[][] theMine;
    private int[] rows = {-1, 0, 1, 0};
    private int[] cols = {0, -1, 0, 1};
    private int minDistance = Integer.MAX_VALUE;

    public RutaCorta(int[][] mine) {
        theMine = mine;
        M = mine.length;
        N = mine[0].length;
    }

    private void markAllUnsafeMineAreas() {
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (theMine[i][j] == 0) {
                    for (int k = 0; k < 4; k++) {
                        if (isSafe(i + rows[k], j + cols[k])) {
                            theMine[i + rows[k]][j + cols[k]] = -1;
                        }
                    }
                }
            }
        }
    }

    public int shortestPath() {
        markAllUnsafeMineAreas();
        int[][] visited = new int[M][];
        for (int count = 0; count < M; count++) {
            visited[count] = new int[N];
        }
        for (int i = 0; i < M; i++) {
            if (theMine[i][0] == 1) {
                findShortestPath(i, 0, visited, 0);
            }
            // if min distance is already found
            if (minDistance == N - 1) {
                break;
            }
        }

        return minDistance;
    }

    private void findShortestPath(int i, int j, int[][] visited, int dist) {
        if (j == N - 1) {
            minDistance = Math.min(dist, minDistance);
            return;
        }
        if (dist > minDistance) {
            return;
        }
        visited[i][j] = 1;

        // Recurse para todos los vecinos adyacentes seguros
        for (int k = 0; k < 4; k++) {
            if (isSafe(i + rows[k], j + cols[k])
                    && visited[i + rows[k]][j + cols[k]] != 1) {
                findShortestPath(i + rows[k], j + cols[k], visited, dist + 1);
            }
        }
        // Borra todos los visitados para ser reutilizados para la próxima iteración
        visited[i][j] = 0;
    }

    private boolean isValid(int i, int j) {
        return (i >= 0 && i <= M - 1 && j >= 0 && j <= N - 1);
    }

    private boolean isSafe(int i, int j) {
        return isValid(i, j) && theMine[i][j] > 0;
    }

    public static void main(String[] args) {
        int mat[][] = {{1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
        {1, 0, 1, 1, 1, 1, 1, 1, 1, 1},
        {1, 1, 1, 0, 1, 1, 1, 1, 1, 1},
        {1, 1, 1, 1, 0, 1, 1, 1, 1, 1},
        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
        {1, 1, 1, 1, 1, 0, 1, 1, 1, 1},
        {1, 0, 1, 1, 1, 1, 1, 1, 0, 1},
        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
        {0, 1, 1, 1, 1, 0, 1, 1, 1, 1},
        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
        {1, 1, 1, 0, 1, 1, 1, 1, 1, 1}};

        // encontrar el camino más corto
        RutaCorta prob = new RutaCorta(mat);
        System.out.println("La longitud de la ruta segura más corta es: " + prob.shortestPath());
    }

}
