#include <limits.h>
#include <math.h>
#include <stdlib.h>

int reverse(int x) {
    if (x <= INT_MIN || x >= INT_MAX) {
        return 0;
    }

    long res = 0;
    int len = floor(log10(abs(x))) + 1;

    // O(d)
    while (len >= 0) {
        res += (x % 10) * pow(10, --len);
        if (res <= INT_MIN || res >= INT_MAX) {
            return 0;
        }

        x /= 10;
    }

    return res;
}
