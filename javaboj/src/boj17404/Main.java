package boj17404;
import java.util.Scanner;
public class Main {
    public static int Solution(int[][] cost, int n){
        int[][] dp = new int[n+1][3];
        dp[1][0]=26;
        dp[1][1]=40;
        dp[1][2]=83;
        for(int i=2 ; i<=n ; i++){
            for(int j=0 ; j<3 ; j++){
                dp[i][j] = dp[i-1][j];
            }
        }
        return 1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n= sc.nextInt();
        int[][] cost = new int[n+1][3];

        for(int i=1 ; i<=n ;i++){
            for(int j=0 ; j<3 ;j++){
                cost[i][j]= sc.nextInt();
            }
        }
        System.out.println(Solution(cost,n));
    }
}
