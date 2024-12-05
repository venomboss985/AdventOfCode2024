// Advent of Code Day 1 - Puzzle 1
#include <stdio.h>

#define ELEMENTS 5

int main(void) {
    FILE *input;
    input = fopen("example.txt", "r");

    int bufl, bufr;
    int left[ELEMENTS];
    int right[ELEMENTS];

    int count = 0;
    while (fscanf(input, "%d%d", &bufl, &bufr) != EOF) {
        left[count] = bufl;
        right[count] = bufr;
        count++;
    }

    int sim = 0;
    for (int i; i < ELEMENTS; i++) {
        // Search for frequency of number
        int frequency = 0;
        for (int j; j < ELEMENTS; j++) {
            frequency += left[i] == right[j];
        }
        printf("Num: %d, Freq: %d\n", left[i], frequency);
        sim += frequency * left[i];
    }
    printf("S: %d\n", sim);
}
