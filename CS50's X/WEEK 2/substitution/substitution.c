#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int key[26];

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution KEY\n");
        return 1;
    }

    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("Key must only contain alphabetic characters.\n");
            return 1;
        }
        else
        {
            for (int j = i + 1; j < 26; j++)
            {
                if (toupper(argv[1][i]) == toupper(argv[1][j]))
                {
                    printf("Key must not contain repeated characters.\n");
                    return 1;
                }
            }
            key[i] = toupper((argv[1][i])) - 65 - i;
        }
    }

    string text = get_string("plaintext: ");

    printf("ciphertext: ");

    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            text[i] = (text[i] + key[toupper(text[i]) - 65]);
            printf("%c", text[i]);
        }
        else
        {
            printf("%c", text[i]);
        }
    }
    printf("\n");
}
