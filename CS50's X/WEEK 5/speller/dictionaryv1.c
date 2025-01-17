// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Represents the number of words in dictionary if loaded
int numword = 0;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    node *cursor = table[hash(word)];

    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }

        cursor = cursor->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open the dictionary file
    FILE *source = fopen(dictionary, "r");

    if (source == NULL)
    {
        printf("Could not open dictionary.\n");
        return false;
    }

    // Buffer space for word
    char *word = malloc (LENGTH + 1);

    // Read each word in the file

    while (fscanf(source, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));

        if (n == NULL)
        {
            return false;
        }

        // Add each word to the hash table
        strcpy(n->word, word);
        n->next = table[hash(word)];
        table[hash(word)] = n;

        numword++;
    }

    // Close the dictionary file
    free(word);
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (numword > 0)
    {
        return numword;
    }
    else
    {
        return 0;
    }
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];

        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;

            free(temp);
        }
    }

    return true;
}
