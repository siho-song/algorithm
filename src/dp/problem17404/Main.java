package dp.problem17404;


import java.io.*;
import java.util.StringTokenizer;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final int INF = 1_000*1_000;
    private static int n;

    private static int answer;
    private static int dp[][];
    private static int rgb[][];

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        answer = INF;
        rgb = new int[n+1][3];
        dp = new int[n+1][3];


        for(int i=1; i<=n ; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0; j<3; j++){
                rgb[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for(int k=0 ; k<3 ;k++){

            for(int i=0; i<3 ;i++){
                if(i == k) {
                    dp[1][i] = rgb[1][i];
                }
                else {
                    dp[1][i] = INF;
                }
            }

            for(int i=2 ; i<=n ; i++){
                dp[i][0] = Math.min(dp[i-1][1],dp[i-1][2]) + rgb[i][0];
                dp[i][1] = Math.min(dp[i-1][0],dp[i-1][2]) + rgb[i][1];
                dp[i][2] = Math.min(dp[i-1][0],dp[i-1][1]) + rgb[i][2];
            }


            for(int i=0; i<3 ; i++){
                if(i != k) answer = Math.min(answer, dp[n][i]);
            }
        }

        System.out.println(answer);

    }
}
