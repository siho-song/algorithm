package bruteforce.problem14500;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int N;
    private static int M;

    private static int max=Integer.MIN_VALUE;

    private static int[][] matrix;

    private static boolean[][] visited;

    private static final int[][] DIRECTION = {{1,0},{-1,0},{0,1},{0,-1}};

    public static void dfs(int startY , int startX,int sum, int depth){

        if(depth == 4){
            max = Math.max(sum,max);
            return;
        }

        for(int[] direction : DIRECTION){
            int newY = startY + direction[0];
            int newX = startX + direction[1];
            if(newY >= 0 && newY <N && newX >=0 && newX<M){
                if(!visited[newY][newX]){

                    //ㅗ 모양 만들기
                    if(depth == 2){
                        visited[newY][newX] = true;
                        dfs(startY,startX,sum+matrix[newY][newX],depth+1);
                        visited[newY][newX] = false;
                    }

                    visited[newY][newX] = true;
                    dfs(newY,newX,sum+matrix[newY][newX],depth+1);
                    visited[newY][newX] = false;
                }
            }
        }
    }


    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        matrix = new int[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                visited[i][j] = true;
                dfs(i,j,matrix[i][j],1);
                visited[i][j] = false;
            }
        }

        System.out.println(max);
    }
}
