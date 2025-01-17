#include <cs50.h>
#include <stdio.h>

void print_row(int spaces, int briks);

int main(void)
{
    int height;
    do0
    {
        height = get_int("Height: ");
    }
    while (height < 1);

    for (int i = 0; i < height; i++)
    {
        print_row(height - i - 1, i + 1);
        printf("\n");
    }
}

void print_row(int spaces, int briks)
{
    for (int i = 0; i < spaces; i++)
        printf(" ");

    for (int i = 0; i < briks; i++)
        printf("#");
}
