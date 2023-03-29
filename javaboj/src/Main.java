import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        long result;

        for (int i=0; i<t;i++){
            int n = sc.nextInt();
            int[] arr = new int[n];
            result =0;
            for(int j=0 ; j<n; j++){
                arr[j] = sc.nextInt();
            }

            for (int k=0 ; k<n ;k ++){
                for(int u = k; u < n-1 ;u++){
                    result +=gcd(arr[k],arr[u+1]);
                }
            }
            System.out.println(result);
        }
    }

    public static int gcd(int num1, int num2){
        if(num1 % num2 ==0){
            return num2;
        }

        return gcd(num2, num1%num2);
    }
//        List<Integer> list;
}




