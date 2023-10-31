#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

int main() {
    char buffer[255];
    char pattern[255];
    int caseSensitive = 1, pos = -1;
    
    printf("Enter a sentence, up to 255 characters.\n");
    fgets(buffer, 255, stdin);
    buffer[strcspn(buffer, "\n")] = '\0'; // remove newline from fgets

    printf("Enter the pattern.\n");
    fgets(pattern, 255, stdin);
    pattern[strcspn(pattern, "\n")] = '\0'; // remove newline from fgets

    printf("1 for case sensitive, 0 for no case sensitive\n");
    scanf("%d", &caseSensitive); // storing input either 0 or 1

    if (caseSensitive == 0) {
        // if input caseSensitive is 0 make everything to lowercase
        for (int i = 0; buffer[i]; i++) {
        buffer[i] = tolower(buffer[i]);
        }
        for (int i = 0; pattern[i]; i++) {
        pattern[i] = tolower(pattern[i]);
        }
    } // case sensitive changer
    // checking each char code block
    //get length of strings
    int mainStrLen = strlen(buffer);
    int patternLen = strlen(pattern);

    for (int i = 0; i <= mainStrLen - patternLen; i++) {
        int x; // declaring x for storing position
        for (x = 0; x < patternLen; x++) {
        char mainStr = buffer[x + i];
        char patternStr = pattern[x];

        if (patternStr == '_') {
            if (!isspace(patternStr)) {
            break;
            }
        }
        else if (patternStr == '.') { /* ignore this since '.' can be any char*/ } 
        else if (patternStr != mainStr) {
            break; // if pattern does not match break out of for loop
        };
        }
        if (x == patternLen) {
        pos = i; // returns first positon found and break out.
        break;
        }
    }
    // printing statements
    if (pos != -1)
    {
        printf("Matches at position %d.\n", pos);
    }
    else
    {
        printf("No match.\n");
    }
    

    return 0;
}
