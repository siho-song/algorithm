package dfsBfs.problem11724;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int nodeNum;
    private static int edgeNum;

    private static boolean[] visited;
    private static ArrayList<ArrayList<Integer>> graph;

    private static int answer=0;

    public static void addEdge(int from, int to){
        graph.get(from).add(to);
    }

    public static void dfs(int start){
        visited[start] =true;
        for (int i : graph.get(start)) {
            if(visited[i] == false){
                dfs(i);
            }
        }

    }

    public static void main(String[] args) throws IOException {

        StringTokenizer st = new StringTokenizer(br.readLine());
        nodeNum = Integer.parseInt(st.nextToken());
        edgeNum = Integer.parseInt(st.nextToken());
        visited = new boolean[nodeNum+1];
        graph = new ArrayList<>();

        int from;
        int to;
        for (int i = 0; i <= nodeNum; i++) {
            graph.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < edgeNum; i++) {
            st = new StringTokenizer(br.readLine());
            from = Integer.parseInt(st.nextToken());
            to = Integer.parseInt(st.nextToken());
            addEdge(from,to);
            addEdge(to,from);
        }

        for (int i = 1; i < nodeNum+1; i++) {

            if(!visited[i]) {
                dfs(i);
                answer++;
            }
        }

        System.out.println(answer);

    }
}
