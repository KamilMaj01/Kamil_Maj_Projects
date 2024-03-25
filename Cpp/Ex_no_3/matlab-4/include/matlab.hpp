#ifndef INCLUDE_MATLAB_HPP_
#define INCLUDE_MATLAB_HPP_

// Biblioteka <cstddef> zawiera definicję typu `std::size_t`.
#include <cstddef>

// Biblioteka <vector> zawiera definicję szablonu klasy `std::vector`.
#include <vector>

#include <string>

class MatVect {
public:
    MatVect(std::size_t n) : v_(n, 0) {}

    MatVect(const std::vector<int>& v) : v_(v) {}

    MatVect(std::string str);  // EXT

    const int& operator[](std::size_t pos) const { return v_[pos]; }
    int& operator[](std::size_t pos) { return v_[pos]; }

    std::vector<int>::const_iterator cbegin() const { return v_.cbegin(); }
    std::vector<int>::const_iterator cend() const { return v_.cend(); }
    std::vector<int>::iterator begin() { return v_.begin(); }
    std::vector<int>::const_iterator begin() const { return v_.cbegin(); }
    std::vector<int>::iterator end() { return v_.end(); }
    std::vector<int>::const_iterator end() const { return v_.cend(); }

    std::size_t size() const { return v_.size(); }

    double norm() const;

    int sum() const;

private:
    std::vector<int> v_;
};

MatVect add_vectors(const MatVect& v1, const MatVect& v2);

std::string to_string(const MatVect& v);

class Matrix {
public:
    Matrix(std::size_t n_rows, std::size_t n_cols) : matrix_(n_rows, MatVect(n_cols)){}
    Matrix(const std::vector<std::vector<int>>& m);

    std::size_t size() const {return matrix_.size();}

    const MatVect& operator[](std::size_t pos) const { return matrix_[pos]; }
    MatVect& operator[](std::size_t pos) { return matrix_[pos]; }

    std::vector<MatVect>::const_iterator cbegin() const { return matrix_.cbegin(); }
    std::vector<MatVect>::const_iterator cend() const { return matrix_.cend(); }
    std::vector<MatVect>::iterator begin() { return matrix_.begin(); }
    std::vector<MatVect>::const_iterator begin() const { return matrix_.cbegin(); }
    std::vector<MatVect>::iterator end() { return matrix_.end(); }
    std::vector<MatVect>::const_iterator end() const { return matrix_.cend(); }

    int sum() const;


private:
    std::vector<MatVect> matrix_;
};

Matrix add_matrices(const Matrix& matrix_1, const Matrix& matrix_2);
std::string to_string(const Matrix& matrix );


#endif /* INCLUDE_MATLAB_HPP_ */
