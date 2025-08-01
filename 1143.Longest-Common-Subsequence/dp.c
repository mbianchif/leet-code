#include <stdlib.h>
#include <string.h>

int max(int a, int b) { return a > b ? a : b; }

int longestCommonSubsequence(char *text1, char *text2) {
    // O(m)
    int m = strlen(text2);

    // O(m)
    int *prev = calloc(m + 1, sizeof(int));
    int *curr = calloc(m + 1, sizeof(int));

    // O(n * m)
    for (int i = 0; text1[i]; i++) {
        for (int j = 1; j <= m; j++) {
            if (text1[i] == text2[j - 1]) {
                curr[j] = 1 + prev[j - 1];
            } else {
                curr[j] = max(prev[j], curr[j - 1]);
            }
        }

        int *temp = prev;
        prev = curr;
        curr = temp;
    }

    int lcs = prev[m];
    free(prev);
    free(curr);
    return lcs;
}
