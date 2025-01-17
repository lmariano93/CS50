#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string text = get_string("Text: ");

    int length = strlen(text);
    float words = 1;
    float letters = 0;
    float sentences = 0;

    for (int i = 0; i < length; i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
        else if (isblank(text[i]))
        {
            words++;
        }
        else if (text[i] == '?' || text[i] == '!' || text[i] == '.')
        {
            sentences++;
        }
    }

    int index = 0.0588 * (letters / words) * 100 - 0.296 * (sentences / words) * 100 - 15.8 + 0.5;

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }

    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }

    else
    {
        printf("Grade %i\n", index);
    }
}
