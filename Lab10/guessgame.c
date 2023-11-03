#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_WORD_LENGTH 12
#define MAX_GUESSES 7

void getValidWord(char *word) {
    while (1) {
        printf("Player 1, enter a word of no more than 12 letters: ");
        fgets(word, MAX_WORD_LENGTH + 1, stdin);
        word[strcspn(word, "\n")] = '\0'; // Remove the newline character

        char *ptr = word;
        int valid = 1;
        while (*ptr) {
            if (!islower(*ptr)) {
                valid = 0;
                break;
            }
            ptr++;
        }

        if (valid && strlen(word) <= MAX_WORD_LENGTH) {
            break;
        } else {
            printf("Sorry, the word must contain only English letters.\n");
        }
    }
}

int main() {
    char word[MAX_WORD_LENGTH + 1];
    getValidWord(word);

    char guessedWord[MAX_WORD_LENGTH * 2]; // Double the length to add spaces
    int guessedWordLen = 0;

    for (int i = 0; word[i]; i++) {
        guessedWord[guessedWordLen++] = '_';
        if (i < strlen(word) - 1) {
            guessedWord[guessedWordLen++] = ' '; // Add space after underscore
        }
    }
    guessedWord[guessedWordLen] = '\0';

    int incorrectGuesses = 0;

    while (1) {
        printf("Player 2 has so far guessed: %s\n", guessedWord);
        printf("Player 2, you have %d guesses remaining. Enter your next guess: ", MAX_GUESSES - incorrectGuesses);

        char guess;
        scanf(" %c", &guess); // Read a single character

        if (islower(guess)) {
            int correctGuess = 0;
            for (int i = 0; word[i]; i++) {
                if (word[i] == guess) {
                    guessedWord[i * 2] = guess;
                    correctGuess = 1;
                }
            }

            if (strcmp(word, guessedWord) == 0) {
                printf("Player 2 wins. The word was: %s\n", word);
                break;
            }

            if (!correctGuess) {
                incorrectGuesses++;
                if (incorrectGuesses >= MAX_GUESSES) {
                    printf("Player 2 has used up all the guesses. Player 1 wins. The word was: %s\n", word);
                    break;
                }
            }
        } else {
            printf("Invalid input. Enter a single lowercase letter from 'a' to 'z'.\n");
        }
    }

    return 0;
}
