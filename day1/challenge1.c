// Advent of Code Day 1 - Puzzle 1
#include <stdio.h>
#include <stdlib.h>

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
    int left[ELEMENTS];
    int right[ELEMENTS];

    int count = 0;
    while (fscanf(input, "%d%d", &bufl, &bufr) != EOF) {
        left[count] = bufl;
        right[count] = bufr;
        count++;
    }

    qsort(left, ELEMENTS, sizeof(int), compare);
    qsort(right, ELEMENTS, sizeof(int), compare);

    int dist = 0;
    for (int i; i < ELEMENTS; i++) {
        dist += abs(left[i] - right[i]);
    }
    printf("D: %d\n", dist);
}
