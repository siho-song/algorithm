package dfsBfs.problem1260;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main{
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int N;
    private static int M;
    private static int start;
    private static ArrayList<ArrayList<Integer>> graph;
    private static ArrayList<Integer> queue;

    private static boolean[] visited;

    private static void dfs(int start){
        visited[start] =true;
        System.out.print(start+" ");
        for(int i : graph.get(start))
            if(visited[i] != true){
                dfs(i);
            }
    }

    private static void bfs(int start){
        visited = new boolean[N+1];
        queue = new ArrayList<>();
        visited[start] = true;
        queue.add(start);
        System.out.println();
        while(!queue.isEmpty()){
            int node = queue.remove(0);
            System.out.print(node + " ");
            for(int i : graph.get(node)){
                if(visited[i] == false){
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        start=Integer.parseInt(st.nextToken());

        graph = new ArrayList<ArrayList<Integer>>();
        visited = new boolean[N+1];
        for(int i=0 ; i<N+1; i++){
            graph.add(new ArrayList<Integer>());
        }

        //undirected graph
        for(int i=0; i<M ; i++){
            st = new StringTokenizer(br.readLine());
            int a=Integer.parseInt(st.nextToken());
            int b=Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        for(int i=1 ; i<N+1; i++){
            Collections.sort(graph.get(i));;
        }

        dfs(start);
        bfs(start);

    }
}
