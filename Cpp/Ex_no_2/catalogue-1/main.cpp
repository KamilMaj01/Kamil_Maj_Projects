#include <iostream>
#include "catalogue.hpp"

int main() {
    Product apple("R4", "apple", 4.5567);
    Product orange("R5", "orange", 8.262626);

    std::cout << to_string(apple) << std::endl;
    std::cout << to_string(orange) << std::endl;

    return 0;
}
