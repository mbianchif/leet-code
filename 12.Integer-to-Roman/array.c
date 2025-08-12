#include <math.h>
#include <stdlib.h>
#include <string.h>

char *intToRoman(int num) {
    char I[10][5] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
    char X[10][5] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
    char C[10][5] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
    char M[10][5] = {"", "M", "MM", "MMM"};

    char *roman = calloc(20, sizeof(char));
    int len = floor(log10(num));

    for (int i = 0; i <= len; i++) {
        int n = (int)(num / pow(10, len-i)) % 10;
        switch (len-i) {
        case 0:
            strcat(roman, I[n]);
            break;
        case 1:
            strcat(roman, X[n]);
            break;
        case 2:
            strcat(roman, C[n]);
            break;
        case 3:
            strcat(roman, M[n]);
            break;
        }
    }

    return roman;
}
