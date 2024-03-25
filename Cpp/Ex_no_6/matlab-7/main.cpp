#include "matlab.hpp"

#include <cstdlib>
#include <iostream>

int main() {
    Matlab::Vector v1(std::vector<int>{1, 3,3});
    Matlab::Vector v2(std::vector<int>{4, 5});
    Matlab::add_vectors(v1,v2);
    std::cout<<"sss"<<std::endl;
    return EXIT_SUCCESS;
}
