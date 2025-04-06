import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        for (int test = 0; test < T; test++) {
            int k = Integer.parseInt(br.readLine());
            String[] arr = new String[k];
            boolean impossible = true;

            for (int i = 0; i < k; i++) {
                arr[i] = br.readLine();
            }

            outer:
            for (int i = 0; i < k; i++) {
                for (int j = 0; j < k; j++) {
                    if (i == j) {
                        continue;
                    }
                    StringBuilder sb = new StringBuilder();
                    sb.append(arr[i]);
                    sb.append(arr[j]);

                    String original = sb.toString();
                    String reversed = sb.reverse().toString();
                    if (original.equals(reversed)) {
                        System.out.println(original);
                        impossible = false;
                        break outer;
                    }
                }
            }
            if (impossible) {
                System.out.println(0);
            }
        }
        br.close();
    }
}
