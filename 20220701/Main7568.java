// 백준 7568

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
 
public class Main7568 {
	public static void main(String[] args) throws IOException {
 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // Scanner보다 빠르다
		
		int tries = Integer.parseInt(br.readLine());
 
		int[][] arr = new int[tries][2];
 
		String[] sp;
		for(int i = 0; i < tries; i++) {
			sp = br.readLine().split(" ");	// 입력받은 문자열 분리
			arr[i][0] = Integer.parseInt(sp[0]);    // 몸무게 
			arr[i][1] = Integer.parseInt(sp[1]);	// 키 
		}
		
		StringBuilder sb = new StringBuilder(); // System.out.println(rank+' ')보다 빠르다

		for(int i = 0; i < tries; i++) {
			int rank = 1;
			
			for(int j = 0; j < tries; j++) {
				if(i == j) { // 자기 자신은 생략함
                    continue;
                }

				if (arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1]) { // 자신보다 덩치가 큰 사람이 있는 경우 rank를 증가시킨다
					rank++;
				}
			}
 
			sb.append(rank).append(' ');
		}
        System.out.println(sb);
	}
}