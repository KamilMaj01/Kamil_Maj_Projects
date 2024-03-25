#include <cstdlib>

#include "vehicles.hpp"
#include <iostream>

int main() {
    Car car("r8", "audi", 100.2);
    std::unique_ptr<Car> driver_1 = std::make_unique<Car>(car);
    Driver kamil("Kamil Maj", std::move(driver_1) );
    std::cout<<to_string(kamil)<<std::endl;
    Driver piotr("piotrek");
    std::cout<<to_string(piotr)<<std::endl;


    return EXIT_SUCCESS;


}
