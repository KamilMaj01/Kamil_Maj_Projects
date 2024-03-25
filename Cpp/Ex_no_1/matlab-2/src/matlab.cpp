#include "matlab.hpp"

// Wersje standardowych bibliotek znanych z języka C, ale zaimplementowanych
// dla C++, mają przedrostek "c". Dołączając je, nie podajemy rozszerzenia ".h".
// Przykładowo: stdlib.h -> cstdlib
#include <cstdlib>

// Biblioteka <iostream> służy do obsługi strumieni wejścia/wyjścia (odpowiednik
// <stdio.h> w języku C).
#include <iostream>

#include <cmath>
MatVect::MatVect(std::size_t n) {
    for (std::size_t i = 0; i < n; i++){
        v_.push_back(0);
    }
}

double MatVect::norm() {
    double sum_of_squares = 0.0;
    for (std::size_t i = 0; i < v_.size(); i++){
        sum_of_squares += v_[i] * v_[i];
    }
    return sqrt(sum_of_squares);
}




MatVect add_vectors(MatVect v1, MatVect v2){
    MatVect v_sum(v1.size());
    for(std::size_t i = 0; i < v1.size(); i++){
        v_sum.set_elem(i, v1.get_elem(i) + v2.get_elem(i));
    }
    return v_sum;
}

void print_vector(int* v, std::size_t n) {
    for (std::size_t i = 0; i < n; i++) {
        std::cout << v[i] << " ";
    }
    std::cout << std::endl;
}
