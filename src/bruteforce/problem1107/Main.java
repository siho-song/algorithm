package bruteforce.problem1107;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static final int START = 100;
    private static final int INF = 1_000 * 1_000;
    private static int end;
    private static int n;
    private static int answer=0;

    private static int length;

    private static boolean[] button = new boolean[10];
    //true == 고장 , false == 정상
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {

        end = Integer.parseInt(br.readLine());
        length = String.valueOf(end).length();
        n= Integer.parseInt(br.readLine());

        int min=INF;
        int cnt= 0;
        int temp;

        if(n >0){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int i=0; i<n ;i++){
                temp = Integer.parseInt(st.nextToken());
                button[temp] = true;
            }
        }

        answer=Math.abs(end-START); //+,- 만으로 움직였을 때

        for(int i=0 ; i<=999999; i++){
            String str = String.valueOf(i);
            int length = str.length();
            boolean isBroken = false;
            for(int j=0 ; j<length ; j++){
                if(button[str.charAt(j)-'0'] == true){
                    isBroken = true;
                    break;
                }
            }
            if(isBroken == true ){
                continue;
            }

            cnt = length + Math.abs(i-end);

            if(cnt < min){
                min = cnt;
            }

        }

        if(min < answer) {
            answer = min;
        }
        System.out.println(answer);
    }
}