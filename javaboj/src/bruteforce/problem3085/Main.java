package bruteforce.problem3085;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;


public class Main {
    private static int N;
    private static char[][] matrix;
    private static int max = 0;
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void swap(char a, char b) {
        char temp = a;
        a = b;
        b = temp;
    }

    public static void arrCheck() {
        // → 가로로 체크
        for(int i=0; i<N; i++) {
            int count = 1;
            for(int j=0; j<N-1; j++) {

                // 이전 사탕과 동일한 경우 -> 계속 먹는다
                if(matrix[i][j] == matrix[i][j+1])
                    count ++;

                    // 이전과 다른 사탕인 경우 -> 새로 먹어야하므로 1로 초기화
                else
                    count = 1;

                // 사탕 최대 개수 저장
                max = Math.max(max, count);
            }
        }

        // ↓ 세로로 체크
        for(int i=0; i<N; i++) {
            int count = 1;
            for(int j=0; j<N-1; j++) {
                if(matrix[j][i] == matrix[j+1][i])
                    count ++;
                else
                    count = 1;
                max = Math.max(max, count);
            }
        }
    }

    public static void main(String[] args) throws IOException {

        Scanner scan = new Scanner(System.in);
        N = scan.nextInt();	// 보드의 크기
        matrix = new char[N][N];

        /* N x N 사탕 입력받기 */
        for(int i=0; i<N; i++) {
            String str = scan.next();
            for(int j=0; j<matrix[i].length; j++) {
                matrix[i][j] = str.charAt(j);
            }
        }

        //가로교환 후 가로세로 체크
        for(int i=0; i<N; i++) {
            for(int j=0; j<N-1; j++) {
                // 가로로 인접한 두 문자 교환
                //swap(matrix[i][j], matrix[i][j+1]);
                char temp = matrix[i][j];
                matrix[i][j] = matrix[i][j+1];
                matrix[i][j+1] = temp;

                // →, ↓ 체크
                arrCheck();

                // 이전에 교환한 문자 복구
                //swap(matrix[i][j], matrix[i][j+1]);
                temp = matrix[i][j];
                matrix[i][j] = matrix[i][j+1];
                matrix[i][j+1] = temp;
            }
        }

        //세로교환 후 가로세로 체크
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N-1; j++) {
                char temp = matrix[j][i];
                matrix[j][i] = matrix[j+1][i];
                matrix[j+1][i] = temp;

                // →, ↓ 체크
                arrCheck();

                // 이전에 교환한 문자 복구
                //swap(board[j][i], board[j+1][i]);
                temp = matrix[j][i];
                matrix[j][i] = matrix[j+1][i];
                matrix[j+1][i] = temp;
            }
        }

        System.out.println(max);

    }
}

