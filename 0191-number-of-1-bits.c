#include <string.h>
#include <stdlib.h>

#include <stdint.h>

int hammingWeight(uint32_t n) {
    int res = 0;
    int bit = 0;
    while (n != 0) {
        bit = n & 1;
        if (bit == 1) {
            res++;
        }
        n = n >> 1;
    }
    return res;
}