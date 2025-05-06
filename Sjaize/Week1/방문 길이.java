// 3차원 배열을 이용하여 방문 처리를 수행할 수 있다.
class Solution {
    static int[] dy = {-1,0,0,1};
    static int[] dx = {0,1,-1,0};
    
    public int solution(String dirs) {
        boolean[][][] visited = new boolean[11][11][4];
        int y = 5, x = 5, d = 0;
        int answer = 0;
        
        for (char command : dirs.toCharArray()) {
            if (command == 'U') d = 0;
            if (command == 'R') d = 1;
            if (command == 'L') d = 2;
            if (command == 'D') d = 3;
            
            int ny = y + dy[d];
            int nx = x + dx[d];
            if (ny < 0 || ny >= 11 || nx < 0 || nx >= 11) continue;
            if (!visited[ny][nx][d]) {
                visited[ny][nx][d] = true;
                visited[y][x][3-d] = true;
                answer++;
            }
            
            y = ny;
            x = nx;
        }
        
        return answer;
    }
}
