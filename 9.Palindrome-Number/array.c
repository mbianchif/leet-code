#include <stdbool.h>

bool isPalindrome(int x) {
    long long rev = 0;
    int acc = x;

    // O(d)
    while (acc > 0) {
        int d = acc % 10;
        acc /= 10;

        rev *= 10;
        rev += d;
    }

    return x == rev;
}
