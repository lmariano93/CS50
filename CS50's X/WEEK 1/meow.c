#include <stdio.h>
#include <cs50.h>

int main (void)
{
    int i=3;
    while (i>0)
    {
        printf("meow\n");
        i--; /* (i--) = (i-=1) = (i=i-1)*/
    }

}

/* Forma mais usual de fazer é a seguir, pois começa a contagem a partir de zero
    int i=0;
    while (i<3)
    {
        printf("meow\n");
        i++;
    }
*/
