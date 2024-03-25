#include <iostream>
#include "complex.hpp"


int main() {
    std::cout << "Hello, World!" << std::endl;
    double  tablica[2] = {1.0, 2.0};
    Complex number(tablica);
    std::function<bool(int, int)> spr;
    spr = [](int a, int b){
        if(a > 2 && b>2 ){
            std::cout<<"Prawdaaa"<<std::endl;
            return true;

        }
        else{
            std::cout<<"niePrawdaaaa"<<std::endl;
            return false;

        }
    };

    if(!spr(0,1)){
        std::cout<<"udalo sie"<<std::endl;
    }

    return 0;
}
