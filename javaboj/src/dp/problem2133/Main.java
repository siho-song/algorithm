package boj2133;
import java.util.Scanner;
public class Main {
    public static int solution(int n){
        int dp[] = new int[31];
        dp[0] = 0;
        dp[1] = 0;
        dp[2] = 3;
        for(int i=4 ; i<n+1 ; i++) {
            int temp = 0;
            if (i % 2 == 1) {
                dp[i] = 0;
            } else {
                dp[i] = dp[i - 2] * 3 + 2;
                for (int j = 1; j < (i - 4) / 2 + 1; j++) {
                    dp[i] = dp[i] + dp[j * 2] * 2;
                }
            }
        }
        return dp[n];
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(solution(n));




    }
}
