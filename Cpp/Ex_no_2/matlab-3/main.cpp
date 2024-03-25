#include "matlab.hpp"
#include <iostream>
#include <cstdlib>

int main() {
    std::vector<int> vec;
    vec.push_back(1);
    vec.push_back(5);
    vec.push_back(2);
    MatVect v1(3);
    MatVect v2(vec);
    v2[0] = 6;

    std::cout << "Elements vec: ";
    for (auto e : vec) { // równowaz˙ne: `for (int e : vec)`
        std::cout << e << " ";
    }
    std::cout << std::endl;

    std::cout << "Elements v1: ";
    for(std::size_t i = 0; i < v1.size(); i++){
        std::cout<<v1[i]<<" ";
    }
    std::cout << std::endl;

    std::cout << "Elements v2: ";
    for(std::size_t i = 0; i < v2.size(); i++){
        std::cout<<v2[i]<<" ";
    }
    std::cout << std::endl;

    to_string(v2);




    return EXIT_SUCCESS;
}
