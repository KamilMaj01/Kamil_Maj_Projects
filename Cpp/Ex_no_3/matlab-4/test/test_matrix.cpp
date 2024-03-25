//
// Created by majka on 10.04.2022.
//

#include "gtest/gtest.h"

#include "matlab.hpp"

TEST(MatlabMatrixTest, toString) {
    Matrix matrix({{1,2},{1,2}});

    std::string str = to_string(matrix);

    ASSERT_EQ(str, "[\n"
                   " [ 1, 2 ],\n"
                   " [ 1, 2 ]\n"
                   "]" );
}

TEST(MatlabMatrixTest, sum) {
    Matrix matrix({{1,2,3},{1,2,3}});

    int sum = matrix.sum();

    ASSERT_EQ(sum, 12);
}