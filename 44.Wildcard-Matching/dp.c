#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

bool isMatch(char *s, char *p) {
    // O(n + m)
    size_t n = strlen(s);
    size_t m = strlen(p);

    bool buf1[m + 1], buf2[m + 1];
    bool *curr = buf1, *prev = buf2;

    // O(m)
    memset(buf1, 0, sizeof(buf1));
    memset(buf2, 0, sizeof(buf2));
    prev[0] = true;

    // O(m)
    for (size_t j = 1; j <= m; j++) {
        prev[j] = p[j - 1] == '*' && prev[j - 1];
        if (!prev[j]) {
            break;
        }
    }

    // O(n * m)
    for (size_t i = 1; i <= n; i++) {
        curr[0] = false;

        for (size_t j = 1; j <= m; j++) {
            curr[j] = false;

            if (s[i - 1] == p[j - 1] || p[j - 1] == '?') {
                curr[j] = prev[j - 1];
            } else if (p[j - 1] == '*') {
                curr[j] = prev[j] || curr[j - 1];
            }
        }

        bool *tmp = prev;
        prev = curr;
        curr = tmp;
    }

    return prev[m];
}
