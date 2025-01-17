#include <cs50.h>
#include <stdio.h>

void print_row(int spaces, int briks);

int main(void)
{
    int change;
    do
    {
        change = get_int("Change owed: ");
    }
    while (change < 1);

    int coins = 0;

    while (change >= 25)
    {
        coins++;
        change -= 25;
    }

    while (change >= 10)
    {
        coins++;
        change -= 10;
    }

    while (change >= 5)
    {
        coins++;
        change -= 5;
    }

    while (change >= 1)
    {
        coins++;
        change--;
    }

    printf("%i\n", coins);
}
