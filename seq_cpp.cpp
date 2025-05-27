#include <iostream>
#include <random>
#include <bitset>
/**
 * generates a 128-bit random sequence using:
 * returns 0 on successful completion of the generation
 */
int main() {
    std::random_device rd;
    std::mt19937 gen(rd());

    std::uniform_int_distribution<> distrib(0, 1);

    std::bitset<128> bits;
    for (int i = 0; i < 128; ++i) {
        bits[i] = distrib(gen);
    }

    std::cout << bits << std::endl;

    return 0;
}
