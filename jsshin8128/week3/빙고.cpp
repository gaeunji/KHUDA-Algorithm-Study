#include <iostream>
using namespace std;

int main() {

    
    pair<int, int> pos[26];
    int board[5][5];
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> board[i][j];
            pos[board[i][j]] = { i,j };
        }
    }

    int calledCount = 0;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            int called;
            cin >> called;
            calledCount++;

            int x = pos[called].first;
            int y = pos[called].second;
            board[x][y] = 0;

            int bingoCount = 0;

            for (int r = 0; r < 5; r++) {
                bool bingo = true;
                for (int c = 0; c < 5; c++) {
                    if (board[r][c] != 0) {
                        bingo = false;
                    }
                }
                if (bingo) {
                    bingoCount++;
                }
            }

            for (int c = 0; c < 5; c++) {
                bool bingo = true;
                for (int r = 0; r < 5; r++) {
                    if (board[r][c] != 0) {
                        bingo = false;
                    }
                }
                if (bingo) {
                    bingoCount++;
                }
            }

            bool diagR = true, diagL = true;
            for (int d = 0; d < 5; d++) {
                if (board[d][d] != 0) {
                    diagR = false;
                }
                if (board[d][4 - d] != 0) {
                    diagL = false;
                }
            }
            if (diagR) {
                bingoCount++;
            }
            if (diagL) {
                bingoCount++;
            }
                
            if (bingoCount >= 3) {
                cout << calledCount << endl;
                return 0;
            }
        }
    }
    return 0;
}
