// Implements a dictionary's functionality

#include <ctype.h>
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
int num_words = 0;

// Number of buckets in hash table
// 26 single digits "a", "b" ...
// 676 double digits "aa", "ab" ...
// 17576 triple digits "aaa", "aab" ...
const unsigned int N = 18278;

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
    int index;

    int len = strlen(word);

    if (len == 1) // 26 single digits "a"
    {
        index = (toupper(word[0]) - 'A');
    }
    else if (len == 2) // 676 double digits "aa", "ab" ...
    {
        index = (toupper(word[0]) - 'A') * 26 + (toupper(word[1]) - 'A');
    }
    else // 17576 triple digits "aaa", "aab" ...
    {
        index = (toupper(word[0]) - 'A') * 676 + (toupper(word[1]) - 'A') * 26 +
                (toupper(word[2]) - 'A');
    }

    return index;
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
    char *word = malloc(LENGTH + 1);

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

        num_words++;
    }

    free(word);

    // Close the dictionary file
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (num_words > 0)
    {
        return num_words;
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
