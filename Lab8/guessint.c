#include <stdio.h>
#include <stdbool.h>

// CONSTANTS
#define LOWEST_NUM 1    // Min num
#define MAX_NUM 1000    // Max num
#define MAX_GUESSES 10  // no of guesses

int main(){
    // VARIABLES
    int player1, player2, guesses = MAX_GUESSES;
    bool win = false, check = false;

    while (!win && guesses > 0)
    {
        if (!check)
        {
            printf("Player 1, enter a number between %d and %d:\n", LOWEST_NUM, MAX_NUM);
            scanf("%d", &player1); // getting input and storing into player1

            // check if number is within range
            if (player1 > MAX_NUM || player1 < LOWEST_NUM)
            {
                // when input is out of range
                printf("That number is out of range.\n");
            }
            else check = true;
        } // if !check
        else
        {
            // if number is within range
            printf("Player 2, you have %d guesses remaining.\n", guesses);
            printf("Enter your guess:\n");
            scanf("%d", &player2); // get input and storing into player2

            // if conditional statement to check if correct guesses
            if (player2 > player1)
            {
                printf("Too high.\n");
                guesses--;
            } // if player2 > player1
            else if (player2 < player1)
            {
                printf("Too low.\n");
                guesses--;
            } // elif player2 < player1
            else if (player2 == player1)
            {
                // player wins
                printf("Player 2 wins\n");
                win = true;
            } // elif player2 == player1
            if (guesses == 0)
            {
                // break out of while loop
                printf("Player 1 wins\n");
                break;
            } // if guesses == 0
        } // else
    } // while
    
    return 0;
} // main
