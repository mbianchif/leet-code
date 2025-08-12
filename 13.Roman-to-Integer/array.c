#include <stdbool.h>
#include <string.h>

bool should_sub(char a, char b) {
    if (b == 'V' || b == 'X') {
        return a == 'I';
    } else if (b == 'L' || b == 'C') {
        return a == 'X';
    } else if (b == 'D' || b == 'M') {
        return a == 'C';
    }

    return false;
}

int romanToInt(char *s) {
    char last_added = 'I';
    int res = 0;

    // O(n)
    int len = strlen(s);

    // O(n)
    for (int i = len - 1; i >= 0; i--) {
        switch (s[i]) {
        case 'I':
            if (should_sub(s[i], last_added)) {
                res -= 1;
            } else {
                res += 1;
            }
            break;
        case 'V':
            if (should_sub(s[i], last_added)) {
                res -= 5;

            } else {
                res += 5;
            }
            break;
        case 'X':
            if (should_sub(s[i], last_added)) {
                res -= 10;
            } else {
                res += 10;
            }
            break;
        case 'L':
            if (should_sub(s[i], last_added)) {
                res -= 50;
            } else {
                res += 50;
            }
            break;
        case 'C':
            if (should_sub(s[i], last_added)) {
                res -= 100;
            } else {
                res += 100;
            }
            break;
        case 'D':
            if (should_sub(s[i], last_added)) {
                res -= 500;
            } else {
                res += 500;
            }
            break;
        case 'M':
            if (should_sub(s[i], last_added)) {
                res -= 1000;
            } else {
                res += 1000;
            }
            break;
        }

        last_added = s[i];
    }

    return res;
}
