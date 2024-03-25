//
// Created by majka on 19.04.2022.
//

#ifndef COMPLEX_1_COMPLEX_HPP
#define COMPLEX_1_COMPLEX_HPP
#include <iostream>
#include <functional>
class Complex {
public:
    Complex(double re, double im) : re_(re), im_(im) {
        std::cout << "Utworzono Complex(re=" << re_ << ", im=" << im_ << ")" << std::endl;
    }
    Complex(double data[2])  : Complex(data[0], data[1]){
        std::cout << "Utworzono Complex [" << data[0]  << " "<<data[1]  <<"]"<< std::endl;}


    double re() const { return re_;}
    double im() const {return im_;}


private:
    double re_;
    double im_;

};

#endif //COMPLEX_1_COMPLEX_HPP
