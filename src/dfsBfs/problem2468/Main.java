package dfsBfs.problem2468;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int N;

    private static int[][] map;
    private static boolean[][] visited;
    private static int maxHeight =0;
    private static int answer =1;

    //상,하,좌,우
    private static final int[][] DIRECTION = {{-1,0},{1,0},{0,-1},{0,1}};

    public static void dfs(int startY, int startX, int height){

        visited[startY][startX] = true;
        for(int[] direction: DIRECTION){
            int newY = startY + direction[0];
            int newX = startX + direction[1];

            if(newX >= 0 && newX < N && newY >=0 && newY <N){
                if(!visited[newY][newX] && map[newY][newX] > height) {
                    dfs(newY, newX,height);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());

        map = new int[N][N];
        visited = new boolean[N][N];

        for(int i=0; i<N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0; j<N; j++){
                int height = Integer.parseInt(st.nextToken());
                map[i][j]= height;
                maxHeight = Math.max(maxHeight,height);
            }
        }


        for(int i=1; i<=maxHeight; i++){
            visited = new boolean[N][N];
            int cnt= 0;
            for(int j=0; j<N ;j++){
                for(int k=0; k<N; k++){
                    if( !visited[j][k] && map[j][k] > i){
                        dfs(j,k,i);
                        cnt++;
                    }
                }
            }
            answer = Math.max(cnt,answer);
        }
        System.out.println(answer);
    }
}
