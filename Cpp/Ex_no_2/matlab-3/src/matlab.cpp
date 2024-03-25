#include "matlab.hpp"

// Wersje standardowych bibliotek znanych z języka C, ale zaimplementowanych
// dla C++, mają przedrostek "c". Dołączając je, nie podajemy rozszerzenia ".h".
// Przykładowo: stdlib.h -> cstdlib
#include <cstdlib>

// Biblioteka <iostream> służy do obsługi strumieni wejścia/wyjścia (odpowiednik
// <stdio.h> w języku C).
#include <iostream>
#include <algorithm>
#include <numeric>



double MatVect::norm() const {
   return sqrt(std::accumulate(std::cbegin(v_), std::cend(v_), 0.0, [](auto acc, auto elem){return acc + elem *elem; }));
}

MatVect add_vectors(const MatVect& v1,const MatVect& v2) {
    MatVect v_sum(v1.size());
    std::transform(v1.cbegin(), v1.cend(), v2.cbegin(), v_sum.begin(), std::plus<>());
    return v_sum;

}


std::string to_string(const MatVect& v){
    std::ostringstream v_string;
    for(const auto& el : v){
        v_string << el << " ";
    }
    std::string v_results = v_string.str();

    return v_results;
}

