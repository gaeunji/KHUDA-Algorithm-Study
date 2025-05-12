import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int[][] board = new int[5][5];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 5; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int num_item = 0;
        for (int i = 0; i < 5; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                num_item = num_item + 1;
                check(Integer.parseInt(st.nextToken()));

                int count = checkRow() + checkCol() + checkDiagonal();
                if (count >= 3) {
                    System.out.println(num_item);
                    br.close();
                    return;
                }
            }
        }
    }

    private static void check(int item) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (board[i][j] == item) {
                    board[i][j] = -1;
                }
            }
        }
    }

    private static int checkRow() {
        int res = 0;
        for (int i = 0; i < 5; i++) {
            int cnt = 0;
            for (int j = 0; j < 5; j++) {
                if (board[i][j] == -1) {
                    cnt++;
                }
            }
            if (cnt == 5) {
                res++;
            }
        }
        return res;
    }

    private static int checkCol() {
        int res = 0;
        for (int i = 0; i < 5; i++) {
            int cnt = 0;
            for (int j = 0; j < 5; j++) {
                if (board[j][i] == -1) {
                    cnt++;
                }
            }
            if (cnt == 5) {
                res++;
            }
        }
        return res;
    }

    private static int checkDiagonal() {
        int res = 0;

        // left to right
        int cnt = 0;
        for (int i = 0; i < 5; i++) {
            if (board[i][i] == -1) {
                cnt++;
            }
        }
        if (cnt == 5) {
            res++;
        }

        // right to left
        cnt = 0;
        for (int i = 0; i < 5; i++) {
            if (board[i][4 - i] == -1) {
                cnt++;
            }
        }
        if (cnt == 5) {
            res++;
        }

        return res;
    }
}
