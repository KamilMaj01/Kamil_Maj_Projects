//
// Created by majka on 19.04.2022.
//
#include "shapes_1.hpp"
#include <ostream>
#include <string>
#include <sstream>

void Shape::to_string() const {
    std::ostringstream oss;
    oss<<"y: "<<y_<<"\n"<<"x: "<< x_;
    std::string result;
    result = oss.str();
    std::cout<<result<<std::endl;

}
