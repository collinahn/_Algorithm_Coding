// 백준 10872

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
 
public class Main10872 {
    private static long factorial(int num) {
        if (num == 0) {
            return 1;
        }
        return num*factorial(num-1);
    }

    public static void main(String[] args) throws IOException {
 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // Scanner보다 빠르다
		
		int num = Integer.parseInt(br.readLine());
 
		
        System.out.println(factorial(num));
	}
}