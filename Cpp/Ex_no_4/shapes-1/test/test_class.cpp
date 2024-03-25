//
// Created by majka on 19.04.2022.
//
#include "gtest/gtest.h"
#include "shapes_1.hpp"

TEST(SquareTest, area) {
Square square(0.0, 0.0, 1.0);
EXPECT_EQ(square.area(), 1.0);

Shape& shape = square;
EXPECT_EQ(shape.area(), 1.0);
}

TEST(CircleTest, area) {
Circle circle(0.0, 0.0, 1.0);
EXPECT_EQ(circle.area(), PI);

Shape& shape = circle;
EXPECT_EQ(shape.area(), PI);
}