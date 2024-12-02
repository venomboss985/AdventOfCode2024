#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define ELEMENTS 1000

int compare(const void* x_void, const void* y_void) {
    int x = *(int*)x_void;
    int y = *(int*)y_void;

    return x - y;
}

int main(void) {
    FILE *input;
    input = fopen("input.txt", "r");

    int bufl, bufr;
    int count = 0;
    int left[ELEMENTS];
    int right[ELEMENTS];

    while (fscanf(input, "%d%d", &bufl, &bufr) != EOF) {
        left[count] = bufl;
        right[count] = bufr;
        count++;
    }

    qsort(left, ELEMENTS, sizeof(int), compare);
    qsort(right, ELEMENTS, sizeof(int), compare);

    // for (int i; i < ELEMENTS; i++) {
    //     printf("L[%d] = %d\n", i, left[i]);
    // }

    int dist = 0;
    for (int i; i < ELEMENTS; i++) {
        dist += abs(left[i] - right[i]);
    }
    printf("D: %d\n", dist);
}
