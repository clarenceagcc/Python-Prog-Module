#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// Prototyping
bool openFile(char *pFileName);

int main()
{   
    char pFileName[20];
    char command[20];
    bool ifExited = false;

    while (!ifExited)
    {
        printf("Welcome to Data Management System!\n");
        printf("Please open your data set file.\n");
        scanf("%s %s", &command, &pFileName); // Storing file name

        if (!openFile(pFileName))
        {
            printf("File does not exist! Try again bitch");
        }
    }
    return 0;
}

bool openFile(char *pFileName) 
{
    // reading file
    FILE *fptr;
    // open file in read mode
    fptr = fopen(pFileName, "r");
    // if file doesnt exist, fptr will be false if file does not exist.
    if (!fptr)
    {
        return false;
    }
    // storing content of txt file
    char bufferStr[255]; // buffer
    while (fgets(bufferStr, 255, fptr) != NULL)
    {
        // printing each line
        printf("%s", bufferStr);
    }
    return true;
}
