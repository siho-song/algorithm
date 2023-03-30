package dfsBfs.problem2667;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main{

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int N;
    private static int[][] map;
    private static boolean[][] visited;


    //상,하,좌,우
    private static final int[][] DIRECTION = {{-1,0},{1,0},{0,-1},{0,1}};
    private static int cnt;
    private static ArrayList<Integer> answer;

    public static void dfs(int startY, int startX){
        visited[startY][startX] = true;
        int newX;
        int newY;
        cnt++;

        for(int[] direction : DIRECTION){
            newY = startY+direction[0];
            newX = startX+direction[1];


            if(newY >=0 && newY < N && newX>=0 && newX<N){
                if(visited[newY][newX] == false && map[newY][newX] ==1)
                {
                    dfs(newY,newX);
                }
            }

        }



    }
    public static void main(String[] args) throws IOException {

        N=Integer.parseInt(br.readLine());

        map = new int[N][N];
        visited = new boolean[N][N];
        answer = new ArrayList<>();


        for(int i=0; i<N ; i++){
            String str = br.readLine();
            for(int j=0; j <N; j++){
                map[i][j] = Integer.parseInt(String.valueOf(str.charAt(j)));
            }
        }

        int startX;
        int startY;
        for(int i=0 ;i<N ;i++){
            for(int j=0; j<N ;j++){
                if(map[i][j] == 1 && visited[i][j] ==false){
                    startY = i;
                    startX = j;
                    cnt=0;
                    dfs(startY, startX);
                    answer.add(cnt);
                }
            }
        }

        Collections.sort(answer);
        System.out.println(answer.size());
        for(int i : answer){
            System.out.println(i);
        }

    }
}