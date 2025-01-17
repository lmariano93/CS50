#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        for (int i = 0, length = strlen(argv[1]); i < length; i++)
        {
            if (!isdigit(argv[1][i]))
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }

        int k = atoi(argv[1]);
        string text = get_string("plaintext: ");
        int length = strlen(text);

        printf("ciphertext: ");

        for (int i = 0; i < length; i++)
        {
            if (isalpha(text[i]))
            {
                if (isupper(text[i]))
                {
                    text[i] = (text[i] + k - 65) % 26 + 65;
                    printf("%c", text[i]);
                }
                else
                {
                    text[i] = (text[i] + k - 97) % 26 + 97;
                    printf("%c", text[i]);
                }
            }
            else
            {
                printf("%c", text[i]);
            }
        }
        printf("\n");
    }
}
