#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

// hashtable item
typedef struct Ht_item
{
    char* key;
    char* value;
} Ht_item;

// Defining hash table
typedef struct HashTable
{
    // Contains an array of pointers to items.
    Ht_item** items;
    int size;
    int count;
} HashTable;

// Prototyping
bool openFile(char *pFileName);
void printTable(HashTable* table);
Ht_item* create_item(char* key, char* value);
HashTable* create_table(int size);
void ht_insert(HashTable* table, char* key, char* value);
unsigned long hash_function(char* str);
void ht_delete(HashTable *table, char *key);

// Constants
#define CAPACITY 50000 // size of Hashtable


int main()
{   
    char pFileName[20];
    char command[20];
    bool ifExited = false;
    HashTable *ht = create_table(CAPACITY);
    printf("TESTING FIRST WITHOUT DELETING\n");
    ht_insert(ht, (char *)"1", (char *)"test1");
    ht_insert(ht, (char *)"2", (char *)"test2");
    printTable(ht);
    printf("----------------------------------\n");
    printf("TESTING AFTER DELETING\n");
    ht_delete(ht, (char *)"1");
    printTable(ht);

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
void ht_insert(HashTable* table, char* key, char* value)
{
    // Creates the item.
    Ht_item *item = create_item(key, value);
    // Computes the index.
    int index = hash_function(key);
    Ht_item *current_item = table->items[index];
    if (current_item == NULL)
    {
        // Insert directly.
        table->items[index] = item;
        table->count++;
    }
}
void ht_delete(HashTable *table, char *key)
{
    int index = hash_function(key);
    Ht_item *item = table->items[index];
    if (item != NULL && strcmp(item->key, key) == 0)
    {
        table->items[index] = NULL;
        table->count--;
    }
}


unsigned long hash_function(char* str)
{
    unsigned long i = 0;
    for (int j = 0; str[j]; j++)
        i += str[j];
    return i % CAPACITY;
}

Ht_item* create_item(char* key, char* value)
{
    // Creates a pointer to a new HashTable item.
    Ht_item* item = (Ht_item*) malloc(sizeof(Ht_item));
    item->key = (char*) malloc(strlen(key) + 1);
    item->value = (char*) malloc(strlen(value) + 1);
    strcpy(item->key, key);
    strcpy(item->value, value);
    return item;
}

HashTable* create_table(int size)
{
    // Creates a new HashTable.
    HashTable* table = (HashTable*) malloc(sizeof(HashTable));
    table->size = size;
    table->count = 0;
    table->items = (Ht_item**) calloc(table->size, sizeof(Ht_item*));
    for (int i = 0; i < table->size; i++)
        table->items[i] = NULL;
    return table;
}

void printTable(HashTable* table)
{
    printf("\nHASH TABLE TEST\n");

    for (int i = 0; i < table->size; i++)
    {
        if (table->items[i])
        {
            printf("Key:%s, Value:%s\n",table->items[i] -> key, table->items[i]->value);
        }
    }
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
