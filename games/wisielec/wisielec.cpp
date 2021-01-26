#include <iostream>
#include <time.h>
#include <cctype>
#include <string>
#include <vector>
#include <algorithm>

using std::cout;
using std::cin;
using std::string;
using std::vector;
using std::endl;
using std::count;
using std::find;

int change(string);
int maks(string tab[]);
int change(string text);
string printLines(string word);


int main()
{
    int chances = 3; // number of chances in game1
    int chance1 = 2; // number of possible mistakes in klik

    /******* interface *******/
    string line0 = "Wybierz, co chcesz zrobic:";
    string line1 = "1. New game";
    string line2 = "2. Exit";
    string lines[3] = { line0, line1, line2 };

    for (int i = 0; i < maks(lines); ++i)
    {
        cout << "#";
    }
    cout << endl << line0 << endl << line1 << endl << line2 << endl;
    for (int i = 0; i < maks(lines); ++i)
    {
        cout << "#";
    }
    cout << endl;
    // frame will be extended in the future
    ////////////////////////////////

    // Data - it could be txt file in the future
    vector<string> animals = { "orka", "lew", "pingwin", "krowa", "skorpion", "mucha", "pies", "konik polny" };
    int animal_len = animals.size();

    // Choosing random number
    srand(time(NULL));
    int random_num = rand() % animal_len - 1;
    string word_to_hangman = animals[random_num];
    // cout << endl << random_num << endl << word_to_hangman << endl;

    // checking the gamer's choice - it should be 1 or 2
    int klik;
    cin >> klik;

    // game:
    if (klik == 1)
    {
        // print lines
        string lines = printLines(word_to_hangman);
        cout << lines << endl; // good :D

        while (chances > 0)
        {
            char letter_from_user;
            cout << "Give a letter: ";
            cin >> letter_from_user;

            for (int i = 0; i < word_to_hangman.length(); ++i)
            {
                if (word_to_hangman[i] == letter_from_user)
                {
                    lines[2 * i] = letter_from_user;
                }
                // cout << lines[2 * i];
                
            }
            cout << lines << endl;
            if (lines.find(letter_from_user) == std::string::npos)
            {
                chances--;

                if (chances >= 2)
                {
                    cout << "You have " << chances << " chances" << endl;
                }
                else if (chances == 1)
                {
                    cout << "You have " << chances << " chance" << endl;
                }
                else
                {
                    cout << "You lost! The word was: " << word_to_hangman << endl;
                }
            }


            if (lines.find("_") == std::string::npos)
            {
                cout << "Wygrana! " << endl;
                exit(0);
            }           
        }
    }
    else if (klik == 2)
    {
        cout << "Exit" << endl;
        exit(0);
    }
    else
    {
        cout << "Wrong number!"; 
    }
}
// change string into length of the string
int change(string text)
{
    return sizeof(text) / sizeof(text[0]);
}

// we are looking for maximum value of length
int maks(string tab[])
{
    int leng = sizeof(tab) / sizeof(tab[0]);
    int maks = change(tab[0]);
    for (int i = 0; i < leng; ++i)
    {
        if (change(tab[i]) < change(tab[i + 1]))
        {
            maks = change(tab[i + 1]);
        }
    }
    return maks;
}

// print lines which represent letters
string printLines(string word)
{
    int word_len = word.length();
    string output = "";


    for (int i = 0; i < word_len; i++)
    {
        if (word[i] == ' ')
        {
            output += ' ';
        }
        else
        {
            output += '_';
            output += ' ';
        }
    }
    return output;
}
