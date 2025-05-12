import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        br.close();

        int[][] table = new int[N][N];
        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};

        int x = 0, y = 0, direction = 0;
        table[x][y] = N * N;

        for (int i = 0; i < N * N - 1; i++) {
            int nx = x + dx[direction];
            int ny = y + dy[direction];

            if (nx == N || ny == N || nx == -1 || ny == -1) {
                direction = (direction + 1) % 4;
                x = x + dx[direction];
                y = y + dy[direction];
                table[x][y] = (N*N - (i+1));
                continue;
            }

            if (table[nx][ny] == 0) {
                x = nx;
                y = ny;
                table[x][y] = (N*N - (i+1));
            }
            else {
                direction = (direction + 1) % 4;
                x = x + dx[direction];
                y = y + dy[direction];
                table[x][y] = (N*N - (i+1));
            }
        }

        int resultX = 0, resultY = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(table[i][j] + " ");
                if (table[i][j] == M) {
                    resultX = i + 1;
                    resultY = j + 1;
                }
            }
            System.out.println();
        }

        System.out.println(resultX + " " + resultY);
    }
}
