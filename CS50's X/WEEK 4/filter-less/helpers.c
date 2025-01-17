#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            uint8_t gray =
                round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);

            image[i][j].rgbtRed = gray;
            image[i][j].rgbtGreen = gray;
            image[i][j].rgbtBlue = gray;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sepia[3];

            sepia[0] = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen +
                             .189 * image[i][j].rgbtBlue);
            sepia[1] = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen +
                             .168 * image[i][j].rgbtBlue);
            sepia[2] = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen +
                             .131 * image[i][j].rgbtBlue);

            for (int k = 0; k < 3; k++)
            {
                if (sepia[k] > 255)
                {
                    sepia[k] = 255;
                }
            }

            image[i][j].rgbtRed = sepia[0];
            image[i][j].rgbtGreen = sepia[1];
            image[i][j].rgbtBlue = sepia[2];
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][j];

            image[i][j] = image[i][width - j - 1];

            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int Red = 0;
            int Green = 0;
            int Blue = 0;

            float sum = 0;

            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    if (i + k < 0 || i + k >= height)
                    {
                        continue;
                    }
                    if (j + l < 0 || j + l >= width)
                    {
                        continue;
                    }

                    Red += copy[i + k][j + l].rgbtRed;
                    Green += copy[i + k][j + l].rgbtGreen;
                    Blue += copy[i + k][j + l].rgbtBlue;

                    sum++;
                }
            }

            image[i][j].rgbtRed = round(Red / sum);
            image[i][j].rgbtGreen = round(Green / sum);
            image[i][j].rgbtBlue = round(Blue / sum);
        }
    }
    return;
}
