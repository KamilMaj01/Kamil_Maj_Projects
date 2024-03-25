#include "matlab.hpp"

// Wersje standardowych bibliotek znanych z języka C, ale zaimplementowanych
// dla C++, mają przedrostek "c". Dołączając je, nie podajemy rozszerzenia ".h".
// Przykładowo: stdlib.h -> cstdlib
#include <cstdlib>

// Biblioteka <iostream> służy do obsługi strumieni wejścia/wyjścia (odpowiednik
// <stdio.h> w języku C).
#include <iostream>

#include <cmath>
#include <sstream>
#include <algorithm>
#include <numeric>

// [OPT]
MatVect::MatVect(std::string str) {
    std::istringstream iss(str);

    std::vector<int> elements;
    int elem;
    while (iss) {
        if (!isdigit(iss.peek())) {
            iss.get();
        } else {
            iss >> elem;
            elements.push_back(elem);
        }
    }

    v_ = elements;
}

double MatVect::norm() const {
    double result;
    result = std::accumulate(std::cbegin(v_), std::cend(v_), 0, [](auto acc,const auto elem){
        return acc + elem * elem ;
    });
        return sqrt(result);
}

MatVect add_vectors(const MatVect& v1, const MatVect& v2) {
    MatVect v_sum(v1.size());

    std::transform(v1.cbegin(), v1.cend(), v2.cbegin(), v_sum.begin(), std::plus<>());

    return v_sum;
}

std::string to_string(const MatVect& v) {
    std::ostringstream oss;

    oss<<"[";
    for(auto it = v.cbegin(); it != v.cend(); it++){
        oss<<" "<<*it<< ((it != v.cend() - 1 ) ? "," : " " );
    }
    oss<<"]";
    return oss.str();
}

Matrix::Matrix(const std::vector<std::vector<int>>& m){
    std::copy(m.cbegin(), m.cend(), std::back_inserter(matrix_) );

}

Matrix add_matrices(const Matrix& matrix_1, const Matrix& matrix_2){
    std::size_t  n_row = matrix_1.size();
    std::size_t  n_col = (matrix_1.size() == 0) ? 0 : matrix_1[0].size();
    Matrix matrix_result(n_row, n_col);
    std::transform(matrix_1.begin(), matrix_1.end() , matrix_2.begin(), matrix_result.begin(), add_vectors);
    return matrix_result;
}
std::string to_string(const Matrix& matrix ){
    std::ostringstream oss;

    oss<<"["<<"\n";
    for(auto it = matrix.cbegin(); it != matrix.cend(); it++ ){
        oss<<" "<< to_string(*it) << ((it != matrix.cend() - 1)  ?  "," : "") << "\n";
    }
    oss<<"]";

    std::string result = oss.str();
    return result;
}

int MatVect::sum() const{
    int result;
    result = std::accumulate(std::begin(v_), std::end(v_), 0);
    return result;

}

int Matrix::sum() const{
    int result_sum;
    result_sum = std::accumulate(std::begin(matrix_), std::end(matrix_), 0, [](auto acc, const auto& v){return acc + v.sum();});
    return result_sum;
}