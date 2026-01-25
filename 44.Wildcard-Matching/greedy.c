#include <stdbool.h>
#include <stdio.h>

bool isMatch(char *s, char *p) {
    size_t i = 0, j = 0;
    size_t saved_s = -1, saved_p = -1;

    // O(n * m)
    while (s[i]) {
        if (s[i] == p[j] || p[j] == '?') {
            i++, j++;
        } else if (p[j] == '*') {
            saved_s = i, saved_p = j++;
        } else if (saved_p != -1) {
            i = ++saved_s, j = saved_p + 1;
        } else {
            return false;
        }
    }

    // O(m)
    while (p[j] == '*') {
        j++;
    }

    return p[j] == '\0';
}
