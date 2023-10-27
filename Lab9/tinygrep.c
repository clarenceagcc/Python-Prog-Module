#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

int main()
{
    char buffer[255];
    char pattern[255];
    int caseSensitive = 1;
    printf("Enter a sentence, up to 255 characters\n");
    fgets(buffer, 255, stdin);
    buffer[strcspn(buffer, "\n")] = '\0'; // remove newline from fgets

    printf("Enter the pattern\n");
    scanf("%s", &pattern);

    printf("1 for case sensitive, 0 for no case sensitive\n");
    scanf("%d", &caseSensitive);

    if (caseSensitive == 1)
    {
        // if input caseSensitive is 1 make everything to lowercase
        for (int i = 0; buffer[i]; i++)
        {
            buffer[i] = tolower(buffer[i]);
        }
    }
    char *position = strstr(buffer, pattern);

    if (position != NULL) {
        int pos = position - buffer;
        printf("Matches at position %d.", pos);
    }
    else {
        printf("No match.");
    }
    
    
    

    return 0;
}
