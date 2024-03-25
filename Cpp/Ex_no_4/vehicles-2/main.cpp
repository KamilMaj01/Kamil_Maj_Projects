#include <cstdlib>

#include "vehicles.hpp"
#include <iostream>

int main() {
    Car car("R0", "audi", 450);
    Car car2("R0", "audi", 450);
    Car car3("R0", "audi", 450);
    Car car4("R0", "audi", 450);
    Bicycle bicycle("r1", "romet", 4);
    Bicycle bicycle2("r1", "romet", 4);
    Bicycle bicycle3("r1", "romet", 4);
    std::cout<< bicycle3.get_vin()<<std::endl;

    return EXIT_SUCCESS;
}
