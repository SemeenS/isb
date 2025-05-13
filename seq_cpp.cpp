#include <iostream>
#include <random>
#include <bitset>

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