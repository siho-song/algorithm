package dfsBfs.problem2178;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;


class Node{
    int x;
    int y;
    public Node(int x ,int y){
        this.x = x;
        this.y =y;
    }
}
public class Main {
    static class Node{
        int x;
        int y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int N;
    private static int M;
    private static final int[] START = {0,0};

    private static int[][] distance ;
    private static ArrayList<Node> queue;
    private static final int[][] DIRECTION ={
            {1,0}, //down
            {-1,0}, //up
            {0,1}, // right
            {0,-1} //left
    };

    private static int min = 1_000 * 1_000;
    private static int[][] maze;
    private static boolean[][] visited;

    private static void bfs(int startX, int startY) {

        visited[startX][startY] = true;
        queue.add(new Node(startX, startY));

        while (!queue.isEmpty()) {
            Node node = queue.remove(0);

            for (int[] direction : DIRECTION) {
                int newX = node.x + direction[0];
                int newY = node.y + direction[1];

                if (newX >= 0 && newX < N
                        && newY >= 0 && newY < M
                        && maze[newX][newY] == 1
                        && visited[newX][newY] == false) {

                    visited[newX][newY] = true;
                    queue.add(new Node(newX,newY));
                    distance[newX][newY] = distance[node.x][node.y] + 1;
                }
            }
        }

    }

    public static void main(String[] args) throws IOException {

        String[] strs = br.readLine().split(" ");
        N=Integer.parseInt(strs[0]);
        M=Integer.parseInt(strs[1]);

        maze = new int[N][M];
        queue = new ArrayList<>();
        visited = new boolean[N][M];
        distance = new int[N][M];
        distance[0][0]=1;

        for(int i=0 ; i<N ; i++){
            String str = br.readLine();
            for (int j = 0; j < M; j++) {
                maze[i][j] = str.charAt(j)-'0';
            }
        }


        bfs(START[0],START[1]);

        System.out.println(distance[N-1][M-1]);

    }
}
