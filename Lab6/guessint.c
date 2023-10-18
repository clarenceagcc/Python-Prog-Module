#include <stdio.h>
#include <stdbool.h>

#define LOWEST_NUM 1    // Min num
#define MAX_NUM 1000    // Max num
#define MAX_GUESSES 10  // no of guesses

int main(){
    int player1, player2, guesses = MAX_GUESSES;
    bool win = false;

    while (!win && guesses > 0)
    {
        printf("Player 1, enter a number between %d and %d:\n", LOWEST_NUM, MAX_NUM);
        scanf("%d", &player1);
        
        if (player1 > MAX_NUM || player1 < LOWEST_NUM)
        {
            printf("That number is out of range.\n");
        }
        else if (player1 < MAX_NUM && player1 > LOWEST_NUM)
        {
            printf("Player 2, you have %d guesses remaining.\n", guesses);
            printf("Enter your guess:\n");
            scanf("%d", &player2);

            if (player2 > player1)
            {
                printf("Too high.\n");
                player2 = -1;
                guesses--;
            }
            else if (player2 < player1)
            {
                printf("Too low.\n");
                player2 = -1;
                guesses--;
            }
            else if (player2 == player1)
            {
                printf("Player 2 wins\n");
                win = true;
            }
        }
    }
    
    
    return 0;
} // main
