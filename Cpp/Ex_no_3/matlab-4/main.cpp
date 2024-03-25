#include "matlab.hpp"

#include <cstdlib>
#include <iostream>

int main() {
    Matrix matrix(3,5);
    Matrix matrix1({{1,2},{1,2}});
    Matrix matrix2({{1,1,1},{1,2,3}});


    std::cout<< to_string(matrix1);
    return EXIT_SUCCESS;
}
