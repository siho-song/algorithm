package bruteforce.problem1476;

import java.io.*;
import java.util.StringTokenizer;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int earth;
    //1<= earth <= 15
    private static int sun;
    //1<= sun <= 28
    private static int month;
    //1<= month <= 19
    private static int answer;
    private static int temp[] = {0,0,0};
    public static void main(String[] args) throws IOException {
        String line = br.readLine();
        StringTokenizer st = new StringTokenizer(line);
        earth = Integer.parseInt(st.nextToken());
        sun = Integer.parseInt(st.nextToken());
        month = Integer.parseInt(st.nextToken());

        while(true){
            temp[0]++;
            temp[1]++;
            temp[2]++;
            if(temp[0]==16){
                temp[0]=1;
            }

            if(temp[1]==29){
                temp[1]=1;
            }

            if(temp[2]==20) {
                temp[2] = 1;
            }
            answer++;
            if(temp[0]==earth && temp[1] == sun && temp[2] == month){
                System.out.println(answer);
                break;
            }
        }
    }
}
