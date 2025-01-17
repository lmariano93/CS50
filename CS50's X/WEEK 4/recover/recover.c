#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");

    if (card == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 1;
    }

    // Create a buffer for a block of data
    BYTE buffer[512];

    // Counter for the name of the JPEGs
    int imgnumber = 0;

    // Allocate space for the name of JPEGs
    char *img = malloc(8 * sizeof(char));

    // Output file
    FILE *output = NULL;

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            ((buffer[3] & 0xf0) == 0xe0))
        {

            // beginning of the first JPEG
            if (imgnumber == 0)
            {
                sprintf(img, "%03i.jpg", imgnumber);
                output = fopen(img, "w");
                fwrite(buffer, 1, 512, output);

                imgnumber++;
            }

            // beginning of others JPEGs
            else
            {
                fclose(output);
                sprintf(img, "%03i.jpg", imgnumber);
                output = fopen(img, "w");
                fwrite(buffer, 1, 512, output);

                imgnumber++;
            }
        }

        // Middle of the JPEGs archives
        else if (imgnumber > 0)
        {
            fwrite(buffer, 1, 512, output);
        }
    }

    free(img);
    fclose(card);
    fclose(output);
}
