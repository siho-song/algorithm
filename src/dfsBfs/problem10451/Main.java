package dfsBfs.problem10451;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    private static int N;
    private static int M;

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int[][] matrix;
    private static ArrayList<ArrayList<Integer>> graph;

    private static boolean[] visited ;

    private static Stack<Integer> stack;

    public static void addNode() throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int k=0; k<M;k++){
            int node = Integer.parseInt(st.nextToken());
            graph.get(k).add(node);
        }
    }

    public static void main(String[] args) throws IOException {

        N= Integer.parseInt(br.readLine());
        for(int i=0 ;i<N ;i++){
            M= Integer.parseInt(br.readLine());
            matrix = new int[N][M];
            graph = new ArrayList<>();
            visited = new boolean[M];
            stack=  new Stack<>();

            int answer=0;

            for(int j=0; j<M; j++){
                matrix[0][j]=j+1;
                graph.add(new ArrayList<Integer>());
            }

            addNode();
            for(int l=0; l<M; l++){

                int start = l;
                if(visited[start]== false){
                    stack.push(start);
                }

                while(!stack.isEmpty()){
                    int next = graph.get(stack.pop()).get(0)-1;
                    if(visited[next] == false){
                        stack.push(next);
                        visited[next] = true;
                    }
                    if(next == start){
                        visited[start] = true;
                        stack.pop();
                        answer++;
                        break;
                    }
                }
            }
            System.out.println(answer);
        }
    }
}
