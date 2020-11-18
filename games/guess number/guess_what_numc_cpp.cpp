/*************************************************************************************/
/******************************* guess random number *********************************/
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <string>
using namespace std;

void create_a_frame(int leng);


int main()
{
    string sentence1 = "# Give me a number in range 1-100  ";
    string sentence2 = "# Write a number which you like: ";
    string sentence3 = "# Wrong number, you have __ chance";
    string sentences[3] = { sentence1, sentence2, sentence3 };
    int LEN = sizeof(sentences) / sizeof(sentences[0]);
    
    // looking for length of frame
    for (int i = 0; i < LEN-1; i++)
    {
        for (int j = 0; j < LEN - i - 1; j++)
        {
            if (sentences[j].length() < sentences[j + 1].length())
            {
                string temp = sentences[j];
                sentences[j] = sentences[j + 1];
                sentences[j + 1] = temp;
            }

        }
        
    }

    // string correct_len = sentences[0];
    string frame_width = sentences[0];
    // cout << frame_width;

    // the random number which should be guessed
    srand(time(NULL));
    int rand_number = rand() % 100 + 1;
    // cout << rand_number;

    /* The moment of game */
    create_a_frame(frame_width.length());
    cout << sentence1;
    int chance = 3;
    while (chance > 0)
    {
        int in_number;
        cin >> in_number;
        if (in_number == rand_number)
        {
            cout << "Great job!";
            cout << endl;
            break;
        }
        else
        {
            if (chance > 2)
            {
                chance--;
                cout << "# Wrong number, you have " << chance << " chances#" << endl;
                string z = (in_number > rand_number) ? "smaller" : "bigger";
                cout << "Random number is " << z << " than yours" << endl;
            }
            else if (chance == 2)
            {
                chance--;
                cout << "# Wrong number, you have " << chance << " chance #" << endl;
                string z = (in_number > rand_number) ? "smaller" : "bigger";
                cout << "Random number is " << z << " than yours" << endl;
            }
            else
            {
                cout << "# Game over, the number was: " << rand_number;
            }
        }


    }
    create_a_frame(frame_width.length());
}

// function that create the frame using the length of string
void create_a_frame(int leng)
{
    for (int i = 0; i < leng; i++)
    {
        cout << "#";
    }
    cout << endl;
}