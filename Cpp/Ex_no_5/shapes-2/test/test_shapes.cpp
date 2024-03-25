#include "gtest/gtest.h"

#include "shapes.hpp"
#include <memory>

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

TEST(ShapesAuxTest, totalAreaOfShapeCollection){
    std::vector<std::unique_ptr<Shape>> vector;
    std::unique_ptr<Square> square = std::make_unique<Square>(0.0, 0.0, 1.0);
    std::unique_ptr<Circle> circle = std::make_unique<Circle>(0.0, 0.0, 1.0);
    vector.push_back(std::move(square));
    vector.push_back(std::move(circle));


    std::vector<Shape*> vector_finish;
    std::transform(vector.begin(), vector.end(), std::back_inserter(vector_finish),
                   [](const std::unique_ptr<Shape>& up) { return up.get(); });
    EXPECT_EQ(calculate_total_area(vector_finish), 1.0 + PI);
}


