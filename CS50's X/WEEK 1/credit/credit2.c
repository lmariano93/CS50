#include <cs50.h>
#include <stdio.h>

int main(void)
{

    long card = get_long("Number: ");

    long sum = 0;

    int length = 0;

//adding the numbers that are not multiplied by 2 and counting them

    for (long i = card; i > 0; i /= 100)
    {
        sum += i % 10;
        length++;
    }

//adding the numbers that are multiplied by 2 and counting them

    for (long i = card / 10; i > 0; i /= 100)
    {
        int remainder = i % 10;
        length++;

        if (remainder < 5)
        {
            sum += 2 * remainder;
        }
        else
        {
            sum += 2 * remainder - 9;
        }
    }

//verifying the card

    sum = sum % 10;

    if (sum == 0)
    {
        if (length == 13)
        {
            long digits = card / 1000000000000;
            if (digits == 4)
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else if (length == 15)
        {
            long digits = card / 10000000000000;
            if (digits == 34 || digits == 37)
            {
                printf("AMEX\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else if (length == 16)
        {
            long digits = card / 100000000000000;
            if (digits > 50 && digits < 56)
            {
                printf("MASTERCARD\n");
            }
            else if (digits / 10 == 4)
            {
                printf("VISA\n");
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
    else
    {
        printf("INVALID\n");
    }
}
