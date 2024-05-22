#include <stdio.h>
#include <iostream>
#include <string>

int main(int argc, char* argv[]) {

    int state[4][4] = {
        {206, 243, 61, 34},
        {171, 11, 93, 31},
        {16, 200, 91, 108},
        {150, 3, 194, 51}
    };

    int round_key[4][4] = {
        {173, 129, 68, 82},
        {223, 100, 38, 109},
        {32, 189, 53, 8},
        {253, 48, 187, 78}
    };

    std::string s("");
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            s += state[i][j] ^ round_key[i][j];
        }
    }

    std::cout << s << '\n';

    return 0;
}