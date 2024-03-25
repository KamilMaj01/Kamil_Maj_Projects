#ifndef INCLUDE_MATLAB_HPP_
#define INCLUDE_MATLAB_HPP_

// Biblioteka <cstddef> zawiera definicję typu `std::size_t`.
#include <cstddef>
#include <vector>


class MatVect {
    public:
        MatVect(std::size_t n);

        int get_elem(std::size_t pos) { return v_[pos]; }
        void set_elem(std::size_t pos, int val) { v_[pos] =  val; }

        std::size_t size() { return v_.size(); }

        double norm();



    private:
    std::vector<int> v_;
};



MatVect add_vectors(MatVect v1, MatVect v2);

void print_vector(int* v, std::size_t n);

#endif /* INCLUDE_MATLAB_HPP_ */
