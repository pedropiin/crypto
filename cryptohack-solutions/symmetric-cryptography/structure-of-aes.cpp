#include <stdio.h>
#include <iostream>
#include <string>

int main(int argc, char* argv[]) {
    int matrix[4][4] = {
        {99, 114, 121, 112},
        {116, 111, 123, 105},
        {110, 109, 97, 116},
        {114, 105, 120, 125}
        };

    std::string res("");
    for (int i = 0; i < 4; i++) {
        for (char c : matrix[i]) {
            res += c;
        }
    }

    std::cout << res << '\n';

    return 0;
}