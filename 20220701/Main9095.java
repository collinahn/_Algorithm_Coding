// 백준 9095 123더하기
// 0부터 1, 2, 3을 더해서 구해지는 각각의 모든 결과에 1, 2, 3을 반복적으로 더하는 과정을 n에 도달할 때 까지 반복한다. 

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
 
public class Main9095 {
    private static int getNumber(int sum, int goal) {
        int cnt = 0;
        if (sum > goal) {
            return cnt;
        }

        if (sum == goal) {
            cnt++;
            return cnt;
        }
        else {
            for (int i = 1; i<=3; i++) {
                cnt += getNumber(sum+i, goal);
            }
            return cnt;
        }
    }

    public static void main(String[] args) throws IOException {
 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // Scanner보다 빠르다
		
        int tempInt;
		int tries = Integer.parseInt(br.readLine());
        for (int i=0; i<tries; i++) {
            tempInt = Integer.parseInt(br.readLine());
            System.out.println(getNumber(0, tempInt));
        }
 
	}
}