import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // 행렬 A 입력받기
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] A = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                int num = Integer.parseInt(st.nextToken());
                A[i][j] = num;
            }
        }

        // 행렬 B 입력받기
        st = new StringTokenizer(br.readLine());
        st.nextToken();
        int K = Integer.parseInt(st.nextToken());
        int[][] B = new int[M][K];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < K; j++) {
                int num = Integer.parseInt(st.nextToken());
                B[i][j] = num;
            }
        }
        br.close();

        // 행렬 곱셈 수행
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < K; j++) {
                int num = 0;
                for (int k = 0; k < M; k++) {
                    num = num + A[i][k] * B[k][j];
                }
                sb.append(num).append(" ");
            }
            if (i < N-1) {
                sb.append("\n");
            }
        }
        System.out.println(sb);
    }
}
