#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Prototypes
void arrayExpressions();
void charAndStrExpressions();
void charAndStrs();

int main()
{
    arrayExpressions();
    charAndStrExpressions();
    charAndStrs();
    return 0;
}

void arrayExpressions()
{
    int a[4] = { -1, 2, 10, 7 };
    int b[4];
    
    for (int i = 0; i < 4; i++){
        b[i] = a[3 - i];
    }

    printf("Array Expressions\n");
    printf("a) %d\n", a[3]);
    printf("b) %d\n", b[3]);
    printf("c) %d\n", b[a[1]]);
}

void charAndStrExpressions()
{
    char *a = "abcdef";
    char b[7];
    strcpy(b, a); // string copy
    for (int i = 0; i < 3; i++){
        b[i] = b[i] + 1;
        b[3] = '\0';
    }

    printf("Character and String Expressions\n");
    printf("a) %c\n", a[0]);
    printf("b) %c\n", b[0]);
    printf("c) %c\n", b[4]);
    printf("d) %d\n", strlen(a)); // strlen gets length of string
    printf("e) %d\n", strlen(b));
    printf("f) %d\n", strcmp(a, b));
    // strcmp compares strings character by character. 
    // If they are exactly the same returns 0
    // If return is > 0 means first non-matching character
    // in a has a greater ASCII value than the corresponding character in b
    // If return is < 0 means first non-matching character
    // in a has a lesser ASCII value than the corresponding character in b
}

void charAndStrs() 
{
    char buffer[255];
    char *token;

    printf("Enter a sentence, up to 255 characters\n");
    fgets(buffer, 255, stdin);

    token = strtok(buffer, " ");
    while (token != NULL)
    {
        printf("\n%s %d", token, strlen(token));
        token = strtok(NULL, " ");
    }

}
