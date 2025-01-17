#include <cs50.h>
#include <stdio.h>

int main(void)
{

    long card = get_long("Number: ");

    long sum = 0;

    // adding the numbers that are not multiplied by 2 and counting them

    for (long i = card; i > 0; i /= 100)
    {
        sum += i % 10;
    }

    // adding the numbers that are multiplied by 2 and counting them

    for (long i = card / 10; i > 0; i /= 100)
    {
        int remainder = i % 10;

        if (remainder < 5)
        {
            sum += 2 * remainder;
        }
        else
        {
            sum += 2 * remainder - 9;
        }
    }

    // verifying the card

    sum = sum % 10;
    int length = 1;
    long digits = 0;

    if (sum == 0)
    {
        for (long i = card; i > 9; i /= 10)
        {
            digits = i;
            length++;
        }
        if ((length == 13 || length == 16) && digits / 10 == 4)
        {
            printf("VISA\n");
        }
        else if ((length == 15 && digits == 34) || digits == 37)
        {
            printf("AMEX\n");
        }
        else if (length == 16 && digits > 50 && digits < 56)
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}
