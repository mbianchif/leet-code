#include <stdbool.h>

bool check_cell(char **board, int row, int col, int boardSize) {
    for (int x = 0; x < 9; x++) {
        if (x != row) {
            if (board[x][col] == board[row][col]) {
                return false;
            }
        }

        if (x != col) {
            if (board[row][x] == board[row][col]) {
                return false;
            }
        }
    }

    int new_row = row - row % 3;
    int new_col = col - col % 3;

    for (int i = new_row; i < new_row + 3; i++) {
        for (int j = new_col; j < new_col + 3; j++) {
            if (i != row && j != col) {
                if (board[i][j] == board[row][col]) {
                    return false;
                }
            }
        }
    }

    return true;
}

bool isValidSudoku(char **board, int boardSize, int *boardColSize) {
    for (int i = 0; i < boardSize; i++) {
        for (int j = 0; j < *boardColSize; j++) {
            if (board[i][j] == '.') {
                continue;
            }

            if (!check_cell(board, i, j, boardSize)) {
                return false;
            }
        }
    }

    return true;
}
