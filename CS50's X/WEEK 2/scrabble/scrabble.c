#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    int points[26] = {1, 3, 3, 2,  1, 4, 2, 4, 1, 8, 5, 1, 3,
                      1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    string word[2];
    int length[2];
    int score = 0;

    for (int i = 0; i < 2; i++)
    {
        word[i] = get_string("Player %i: ", i + 1);
        length[i] = strlen(word[i]);
    }

    for (int i = 0; i < length[0]; i++)
    {
        if (isalpha(word[0][i]))
        {
            score += points[toupper(word[0][i]) - 65];
        }
    }

    for (int i = 0; i < length[1]; i++)
    {
        if (isalpha(word[1][i]))
        {
            score -= points[toupper(word[1][i]) - 65];
        }
    }

    if (score == 0)
    {
        printf("Tie\n");
    }
    else if (score > 0)
    {
        printf("Player 1 wins\n");
    }
    else
        printf("Player 2 wins\n");
}
